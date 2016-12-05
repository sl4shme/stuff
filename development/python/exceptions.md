##Links:
- https://docs.python.org/2.7/tutorial/errors.html
- https://docs.python.org/3/tutorial/errors.html


- https://www.programiz.com/python-programming/exception-handling
- https://www.tutorialspoint.com/python/python_exceptions.htm
- https://openclassrooms.com/courses/apprenez-a-programmer-en-python/les-exceptions-4
- http://sametmax.com/gestion-des-erreurs-en-python/

##Exceptions
When python encounters an error, it raises an exception.
```python
print(1 // 0)
```
> ```
Traceback (most recent call last):
  File "p.py", line 1, in <module>
    print(1 // 0)
ZeroDivisionError: integer division or modulo by zero
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
    raise(IndexError("My exception's Message"))   # specific exception
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
def functions_that_divides(i, j):
    assert j != 0, "This is bad math"
    return i // j

functions_that_divides(1,0)
```
> AssertionError: This is bad math

##Try, Except, Else, Finally
Syntax:
```python
try:
    # Something that could fail
except:
    # What to do if it fails
```

Complete syntax:
```python
try:
    Something that could fail
except IndexError as e:
    # What we want to do if an IndexError happens in the try clause
    raise e
except (TypeError, NameError):
    # We can group exception types
    pass
except:
    # Or catch all exceptions
    pass
else:
    # Runs only if the code in try raises no exceptions
    # Must follow all except clause
finally:
    #  Executed under all circumstances
```

##Built-in exceptions


##Exception objects


##Stacktrace and Traceback


##Python2 and Python3
- http://python-future.org/compatible_idioms.html
