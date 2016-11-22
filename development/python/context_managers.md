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
with open("some_file", "r") as f:
    for number, line in enumerate(f):
        print('{} : {}'.format(number, line))
```

The bad way
```python
files = []
for x in range(100000):
        files.append(open('foo.txt', 'w'))
```
> IOError: [Errno 24] Too many open files: 'foo.txt'

Opening a file consumes a resource (File Descriptor) and the OS imposes a limit
on the maximum of file opened by a process at the same time (you can get he
value with the command:  `ulimit -n`)

When opening a file, the OS assings an integer to the opem file, giving you a
handle to the open file, rather than access to the underlying file>
```python
f = open("./cp2.pdf")
print(f.fileno())
```
> 10



A file descriptor


