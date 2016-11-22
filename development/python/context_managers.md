##Links
 - https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

 - http://sametmax.com/les-context-managers-et-le-mot-cle-with-en-python/
 - https://gist.github.com/bradmontgomery/4f4934893388f971c6c5
 - http://effbot.org/zone/python-with-statement.htm
 - http://stackoverflow.com/questions/32379147/understanding-the-python-with-statement
 - https://docs.python.org/3.5/reference/datamodel.html#context-managers


## Example: Opening a file
The good way of opening a file
```python
with open("plop.txt", "r") as f:
    for number, line in enumerate(f):
        print('{} : {}'.format(number, line))
```

The bad way
```python
files = []
for x in range(100000):
        files.append(open('plop.txt', 'w'))
```
> IOError: [Errno 24] Too many open files: 'foo.txt'

Opening a file consumes a resource (File Descriptor) and the OS imposes a limit
on the maximum of file opened by a process at the same time (you can get he
value with the command:  `ulimit -n`)

When opening a file, the OS assings an integer to the opem file, giving you a
handle to the open file, rather than access to the underlying file>
```python
f = open("plop.txt")
print(f.fileno())
```
> 10

To solve the issue, every `open()`-ed needs to be `close()`-ed.
```python
files = []
for x in range(10000):
        f = open('plop.txt', 'w')
            f.close()
                files.append(f)
```

Sometime, it is hard to ensure that each file will be closed, especially when
dealing with exceptions or with functions with multiple return paths.

This is where context managers come in handy.


## Context managers

```python
with something_that_returns_a_context_manager() as my_resource:
    do_something(my_resource)
    print('done using my_resource')
```

`with` allow us to call anything that returns a context manager (for example the
`open()` function) and assign it to a variable using `as <variable_name>`.
This variable only exists within the indented block below the with statement.
Finaly, when this variable goes out of scope, a special method is called to
cleanup the resource.
This cleanup will happen even if the code block inside the `with` `raise` an
exception, or `return`, or uses `continue` or `break`.

Here is how to create a context manager that mimics `open()`
```python
class My_Context_Manager():

    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.opened_file = open(self.path, self.mode)
        return self.opened_file

    def __exit__(self, *args):
        self.opened_file.close()

with My_Context_manager("plop.txt") as f:
    f.write("Plop !")
```

 The standard library makes use of context managers in many places, basicaly
 wherever an object needs to be closed after usage.
 For example:
  - threading.Lock
  - subprocess.Popen
  - tarfile.TarFile
  - pathlib.Path
  - ...


## Enter() and close()

The __enter__() magic method of a context manager should not expect any
parameter. What it return is what will be saved in the variable specified with
the `as` keyword.

Using `as` is not mandatory, in some case, we don't need to access the resource
returned by the context manager (Lock for example).

The __exit__() magic method should expect three arguments:
 - type
 - value
 - traceback

If the code in the with block exits without raising any exception, the value
passed are None.

Otherwise they contain informations about the exception (the same you would get
by calling sys.exc_info).

For example if we wanted to write a header and footer to a print, we could use:
```python
class ctx():
    def __enter__(self):
        print("haha")
    def __exit__(self, *arg):
        print("hoho")

with ctx():
	print("test")
```
> haha <br/>
> test <br/>
> hoho <br/>


## The contextlib

The contextlib standard library module contains tooles for creating and working
with context managers.

For example, it contains the @contextmanager decorator.
It is meant to decorate a generator function that calls yied exactly once.
Everything before the call to `yield` is considered the  __enter__().
Everything after is considered __exit__().

Let's rewrite the previous example using this technique
```python
from contextlib import contextmanager

@contextmanager
def my_context_manager(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()


with my_context_manager('plop.txt', 'w') as f:
    f.write("Plop !")
```

The contextlib also contains a base class (Python 3 only) to inherit to create
a context manager that can be used normaly with `with` or as a decorator to a
function.

```python
from contextlib import ContextDecorator

class kawaii(ContextDecorator):
    def __enter__(self):
        print('.+.+.+.+.+.+.')
        return self

    def __exit__(self, *arg):
        print('.+.+.+.+.+.+.')
        return False

@kawaii()
def print_plop():
    print("Plop !")

with kawaii():
    print("Test")

```
> .+.+.+.+.+.+.<br/>
> Plop ! <br/>
> .+.+.+.+.+.+.<br/>
> .+.+.+.+.+.+.<br/>
> Test <br/>
> .+.+.+.+.+.+.<br/>
