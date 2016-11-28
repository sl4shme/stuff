##Links
- https://docs.python.org/3.5/reference/compound_stmts.html#the-if-statement
- https://docs.python.org/3.5/library/stdtypes.html#truth-value-testing

##Comparison Functions
```python
1 == 2
```
> False

```python
1 != 2
```
> True

```python
1 > 2
```
> False

```python
1 < 2
```
> True

```python
1 >= 2
```
> False

```python
1 <= 2
```
> True

```python
"plop" in "dhwejdhwekdewplopdjwekldjewlk"
```
> True

```python
1 not in [1, 2, 3]
```
> False

```python
1 is None
```
> False

```python
1 is not None
```
> True

##`is` vs. `==`
- `is` checks if two variables refer to the same object.
- `==` checks if the objects pointed to have the same values.
```python
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = a             # Point b at what a is pointing to
b is a            # => True, a and b refer to the same object
b == a            # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal
```

##If
```python
if 1 == 1:
    print("PLOP")
```
> PLOP

##If .. else
```python
if 1 > 2:
    print("PLOP")
else:
    print("PLIP")
```
> PLIP

##If .. elif .. else
```python
test = 1
if test == 0:
    print("PLOP")
elif test == 1 :
    print("PLIP")
else:
     print("PLUP")
```
> PLIP

##Using functions
```python
def test():
    return True

if test():
    print("test")
```
> test


##What is False and what is True
Any object can be tested for truth value, for use in an if or while condition or as operand of the Boolean operations below. The following values are considered false:

- None
- False
- Zero of any numeric type, for example, 0, 0.0, 0j.
- Any empty sequence, for example, '', (), [].
- Any empty mapping, for example, {}.
- Instances of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns the integer zero or bool value False.

All the rest is considered True

```python
if "false":
    print("test")
```
> test

```python
if "":
    print("test")
```
> _

##And / or / not
```python
if (1 == 1) and False:
    print("plop")
```
> _

```python
if (1 == 1) or False:
    print("plop")
```
> plop

```python
if (1 == 1) and not False:
    print("plop")
```
> plop
