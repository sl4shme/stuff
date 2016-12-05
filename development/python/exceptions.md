##Links:
- https://docs.python.org/2.7/tutorial/errors.html
- https://docs.python.org/3/tutorial/errors.html 


- https://www.programiz.com/python-programming/exception-handling
- http://python-future.org/compatible_idioms.html

##Exceptions
When python encounters an error, it raises an exception.
```python

Here insert exception example
```

##Raising an exception
Exceptions are raise in two ocasions.

When an error happens:
```python
print(5 / 0)
```
> ZeroDivisionError: integer division or modulo by zero

When we specificaly `raise` one:
```python
if something:
	e = Exception("My exception's Message")   # base exception
    raise(e)
	# Or in one line
    raise(IndexError("My exception's Message"))   # speceific exception
```
> Exception: My exception's Message

##Assert
Assert statements can be compared to a "raise-if-not" statements.
Assertions are a way to check that the internal state of a program is as the
programmer expected.
If the provided condition evaluates to False, an `AssertionError` is raised.

It is possible to bypass all assert statements in a program by passing
the -O argument to the python interpreter.

Syntax:
```python
assert <condition>[, <message>]

```

Example:
```python
def functions_that_divides(i, j)
    assert j != 0, "This is bad math"
    return i // j

functions_that_divides(1,0)
```
> AssertionError: This is bad math

##Try, Except, Else, Finally
```python
try:
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 #  Execute under all circumstances
    print("We can clean up resources here")
```

##Built-in exceptions


##Exception objects


##Stacktrace
