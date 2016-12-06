##Links:
- https://docs.python.org/2.7/tutorial/errors.html
- https://docs.python.org/3/tutorial/errors.html
- https://docs.python.org/3.5/library/warnings.html

##Exceptions
When python encounters an error, it raises an exception.
This exception (if not catched) stops the execution of the program and tries to
provide informations about what happened.

Syntax of what is printed:
```
Traceback
Traceback
Traceback
Traceback
ExceptionName: Description of the problem
```

```python
print(1 // 0)
```
> ```
Traceback (most recent call last):
  File "p.py", line 1, in <module>
    print(1 // 0)
ZeroDivisionError: integer division or modulo by zero
```

```python
if a == 3
    print("Plop")
```
> ```
  File "p.py", line 1
    if a == 3
            ^
SyntaxError: invalid syntax
```

##Traceback
Let's consider a python file:
```
def function_1():
    return 1 / 0

def function_2():
    function_1()

def function_3():
    function_2()

if __name__ == "__main__":
    function_3()
```
> ```
Traceback (most recent call last):
  File "p.py", line 11, in <module>
    function_3()
  File "p.py", line 8, in function_3
    function_2()
  File "p.py", line 5, in function_2
    function_1()
  File "p.py", line 2, in function_1
    return 1 / 0
ZeroDivisionError: division by zero
```

A traceback is read from bottom to top and shows the chain of causality of the error.

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
    # Will catch all other exceptions
    pass
else:
    # Runs only if the code in try raises no exceptions
    # Must follow all except clause
finally:
    #  Executed under all circumstances
```

##Re-raising an exception
```python
try:
    1 / 0
except:
    print("You can't do math")
    raise
```
> ```
You can't do math
Traceback (most recent call last):
  File "p.py", line 2, in <module>
      1 / 0
      ZeroDivisionError: division by zero
```

##Built-in exceptions

Python comes with a multitude of built-in exceptions:

| Name | Cause |
| ---- | ----- |
| ArithmeticError | The base class for those built-in exceptions that are raised for various arithmetic errors |
| AssertionError | Raised when an assert statement fails |
| AttributeError | Raised when attribute assignment or reference fails |
| BaseException | The base class for all built-in exceptions. It is not meant to be directly inherited by user-defined exceptions |
| BufferError | Raised when a buffer related operation cannot be performed |
| EOFError| Raised when one of the built-in functions (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data |
| EnvironmentError | The base class for exceptions that can occur outside the Python system: IOError, OSError |
| Exception | All built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class |
| FloatingPointError | Raised when a floating point operation fails |
| GeneratorExit | Raised when a generator‘s close() method is called, technically not an error |
| IOError | Raised when an I/O operation (ex: print(), open()) fails for an I/O-related reason, e.g., “file not found” or “disk full” |
| ImportError | Raised when an import statement fails to find the module definition or when a from ... import fails to find a name that is to be imported |
| IndentationError | Base class for syntax errors related to incorrect indentation |
| IndexError | Raised when a sequence subscript is out of range. (**Slice indices are silently truncated**) |
| KeyError | Raised when a mapping (dictionary) key is not found in the set of existing keys |
| KeyboardInterrupt | Raised when the user hits the interrupt key (normally Control-C) |
| LookupError | The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid |
| MemoryError | Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects) |
| NameError | Raised when a local or global name is not found |
| NotImplementediError | Abstract methods should raise this exception when they require derived classes to override the method |
| OSError | This exception is derived from EnvironmentError. It is raised when a function returns a system-related error |
| OverflowError | Raised when the result of an arithmetic operation is too large to be represented |
| ReferenceError | Raised when a weak reference proxy is used to access an attribute of the referent after it has been garbage collected |
| RuntimeError | Raised when an error is detected that doesn’t fall in any of the other categories |
| StopIteration | Raised by an iterator‘s next() method to signal that there are no further values |
| SyntaxError | Raised when the parser encounters a syntax error |
| SystemError | Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope |
| SystemExit | Raised by the sys.exit() function. When it is not handled, the Python interpreter exits. If an int is passed, it will be the return code |
| TabError | Raised when indentation contains an inconsistent use of tabs and spaces |
| TypeError | Raised when an operation or function is applied to an object of inappropriate type |
| UnboundLocalError | Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable |
| UnicodeDecodeError | Raised when a Unicode-related error occurs during decoding |
| UnicodeEncodeError | Raised when a Unicode-related error occurs during encoding |
| UnicodeError | Raised when a Unicode-related encoding or decoding error occurs |
| UnicodeTranslateError | Raised when a Unicode-related error occurs during translating |
| ValueError | Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value |
| ZeroDivisionError | Raised when the second argument of a division or modulo operation is zero |

Python2 Only

| Name | Cause |
| ---- | ----- |
| StandardError | The base class for all built-in *error* exceptions, itself is derived from Exception |

Python3 Only

| Name | Cause |
| ---- | ----- |
| Warnings | _ |
| BlockingIOError | _ |
| BrokenPipeError | _ | 
| ChildProcessError | _ | 
| ConnectionAbortedError | _ | 
| ConnectionError | _ | 
| ConnectionRefusedError | _ | 
| ConnectionResetError | _ | 
| FileExistsError | _ | 
| FileNotFoundError | _ | 
| InterruptedError | _ | 
| IsADirectoryError | _ | 
| NotADirectoryError | _ | 
| PermissionError | _ | 
| ProcessLookupError | _ | 
| RecursionError | _ | 
| ResourceWarning | _ | 
| StopAsyncIteration | _ | 
| TimeoutError | _ | 

Python2 Hierarchy
```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
```

Python3 Hierarchy
```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

##User defined exception
Exceptions are created by inheriting the Exception class.
```python
class ValueTooSmallError(Exception):
	"""Raised when input is too small for my program"""
	pass

i = input()
try:
	if i < 5:
		raise(ValueTooSmallError)
except ValueTooSmallError:
    print("This is too small")
```

##Exception objects
Most exceptions will pass a list of arguments that can be used when catching the exception.
```python
try:
    f = open("plop")
except IOError as e:
    print("args: ", e.args)
    print("errno: ", e.errno)
    print("filename: ", e.filename)
    print("strerror: ", e.strerror)
```
> ('args: ', (2, 'No such file or directory')) <br/>
> ('errno: ', 2) <br/>
> ('filename: ', 'plop') <br/>
> ('strerror: ', 'No such file or directory')

Raising with arguments:
```python
try:
    raise(Exception("Plop", "Test", "Toto"))
except exception as e:
    print(e.args)
    raise
```
> ("Plop", "Test", "Toto") <br/>
> Exception: ("Plop", "Test", "Toto")


##Catch all exception of a program
It is possible to catch all non managed (non catched) exception of a program using:
```
import sys

def catch_them_all(type, value, traceback):
    print("Pokemon !")

sys.excepthook = catch_them_all

1 / 0
```
> Pokemon !

##Warnings

Warning messages are typically issued in situations where it is useful to alert the user of some condition in a program, where that condition (normally) doesn’t warrant raising an exception 
and terminating the program. For example, one might want to issue a warning when a program uses an obsolete module.

Warnings can be issued by calling the warn() function.
```python
from warnings import warn

warn("Test")
warn("Test2", SyntaxWarning)
warn(SyntaxWarning("test3"))

print("Still executed")
```
> ```
p.py:3: UserWarning: Test
  warn("Test")
p.py:4: SyntaxWarning: Test2
  warn("Test2", SyntaxWarning)
p.py:5: SyntaxWarning: test3
  warn(SyntaxWarning("test3"))
Still executed
```

Here is the list of Built-in warnings category:

| Name | Description |
| ---- | ----------- |
| BytesWarning | Base category for warnings related to bytes and bytearray |
| DeprecationWarning | Base category for warnings about deprecated features (ignored by default) |
| FutureWarning | Base category for warnings about constructs that will change semantically in the future |
| ImportWarning | Base category for warnings triggered during the process of importing a module (ignored by default) |
| PendingDeprecationWarning | Base category for warnings about features that will be deprecated in the future (ignored by default) |
| ResourceWarning | Base category for warnings related to resource usage |
| RuntimeWarning | Base category for warnings about dubious runtime features |
| SyntaxWarning | Base category for warnings about dubious syntactic features |
| UnicodeWarning | Base category for warnings related to Unicode |
| UserWarning | The default category for warn() |
| Warning | This is the base class of all warning category classes. It is a subclass of Exception |

The warnings filter controls whether warnings are ignored, displayed, or turned into errors (raising an exception).

Simplefilter inserts an entry into the list of warnings filter specifications. The entry is inserted at the front by default; if append is true, it is inserted at the end.
```python
warnings.simplefilter(action, category=Warning, lineno=0, append=False)
```

action can be:

| value | decription |
| ----- | ---------- |
| error | turn matching warnings into exceptions |
| ignore | never print matching warnings |
| always | always print matching warnings |
| default | print the first occurrence of matching warnings for each location where the warning is issued |
| module | print the first occurrence of matching warnings for each module where the warning is issued |
| once | print only the first occurrence of matching warnings, regardless of location |

Resetwarnings resets the warnings filter.
```python
warnings.resetwarnings()
````


##Traceback module

- https://docs.python.org/2/library/traceback.html
- https://docs.python.org/3.5/library/traceback.html

##Python2 and Python3

- http://python-future.org/compatible_idioms.html#raising-exceptions
