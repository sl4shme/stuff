##Links
 - https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/
 - http://preshing.com/20110920/the-python-with-statement-by-example/
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
This cleanup will happen even if the code block inside the `with` raises an
exception.

Here is how to create a context manager that mimics `open()`
```python
class My_Context_manager():

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


