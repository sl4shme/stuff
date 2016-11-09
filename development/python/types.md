##Booleans
Booleans are immutable
```python
a = True
b = False
type(a)
```
> bool

##Numbers
Ints, Floats and Complexes are immutable
Don't bother with longs, in Python they're ints
```python
i = 42
f = 42.42
type(i)
type(f)
```
> int <br/>
> float

```python
float(i)
```
> 42.0

```python
int(f)
```
> 42

##Lists
Lists are mutable
```python
l1 = [1, 2, 3, 4, 5, 6]
l2 = [1, "plop", 42.42, [1, 2, 3]]
print(l2[2])
print(l1[1:3])
print(l1[3:])
print(l1[-1])
```
> 42.42 <br/>
> [2, 3] <br/>
> [4, 5, 6] <br/>
> 6

```python
l2[0] = 0
print(l2)
```
> [0, 'plop', 42.42, [1, 2, 3]]

```python
print(min(l1))
print(max(l1))
```
> 1 <br/>
> 6

```python
del l2[0]
print(l2)
```
> ['plop', 42.42, [1, 2, 3]]

```python
print(len(l1))
```
> 6

```python
print([1, 2, 3] + [4, 5, 6])
```
> [1, 2, 3, 4, 5, 6]

```python
print(3 in [1, 2, 3])
print(l1.index(1))
print(l1.count(1))
```
> True <br/>
> 0 <br/>
> 1

```python
l1.append(7)
print(l1)
```
> [1, 2, 3, 4, 5, 6, 7]

```python
print(l1.pop())
print(l1)
```
> 7 <br/>
> [1, 2, 3, 4, 5, 6]

```python
l1.insert(0, 0)
print(l1)
l1.remove(6)
print(l1)
```
> [0, 1, 2, 3, 4, 5, 6] <br/>
> [0, 1, 2, 3, 4, 5]

```python
l1.reverse() # Reverses the list, does not return the reversed list
print(l1))
print(reversed([1,2,3]))
```
> [5, 4, 3, 2, 1, 0] <br/>
> [3,2,1]

##Tuples
Tuples are immutable
```python
t1 = (1,2,3)
t2 = (4,5,6)
print(t1[0])
print(t1[-1])
```
> 1 <br/>
> 3

```python
print(len(t1))
```
> 3

```python
print(t1+t2)
```
> (1, 2, 3, 4, 5, 6)

```python
print(3 in t1)
print(t1.count(1))
print(t1.index(1))
```
> True <br/>
> 1 <br/>
> 0

```python
t = 1, 2, 3
print(t)
```
> (1, 2, 3)

##Ranges
In Python 2, range() returns a list
in Python3 range is similar to Python2 xrange() and returns a range type object

Ranges implement all of the common sequence operations except concatenation and
repetition

**range([start], stop[, step])**
- _Start_: Starting number of the sequence.
- _Stop_: Generate numbers up to, but not including this number.
- _Step_: Difference between each number in the sequence.

```python
r = range(0,12,2)
for i in r:
    print(i)
```
> 0 <br/>
> 2 <br/>
> 4 <br/>
> 6 <br/>
> 8 <br/>
> 10

```python
print(1 in r)
```
> False

##Sets
```python
s1 = {1, 2, 3, 3, 3}
s2 = {1, 'a', "plop"}
print(s1)
```
> {1, 2, 3}

```python
s1.add(0)
s1.remove(3)
print(s1)
```
> {0, 1, 2}

```python
len(s1)
```
> 3

```python
1 in s1
```
> True

```python
s1 = {0,1,2}
s2 = {2,3,4}
print(s1.difference(s2))           # In s1 but not in s2
print(s1.symmetric_difference(s2)) # Not in both
print(s1.intersection(s2))         # In both
print(s1.union(s2))                # In s1 or s2
```
> {0, 1} <br/>
> {0, 1, 3, 4} <br/>
> {2} <br/>
> {0, 1, 2, 3, 4}

```python
print(s1.isdisjoint(s2)) # No common elements
print(s1.issubset(s2))   # All s1 elements are also part of s2
print(s1.issuperset(s2)) # All s2 elements are also part of s1
```
> False <br/>
> False <br/>
> False

##Frozensets
Frozensets are like sets but immutable and don't have the add() and remove() methods
```python
a = frozenset([1,2,3])
print(a)
```
> frozenset({1, 2, 3})

##Dictionaries
- Dict are non-ordered but their order is static
- No duplicate key
- Keys can be: from any mutable types
- Dicts are mutable

```python
d = {"name": "memo", "sex": "male", "age": 25}
print(d)
```
> {'age': 25, 'name': 'memo', 'sex': 'male'}

```python
d['name'] = "m3m0"
d['height'] = 1.75
print(d)
```
> {'age': 26, 'height': 1.75, 'name': 'm3m0', 'sex': 'male'}

```python
print(d['age'])
print(d.get("age"))
print(d.get("plop", "nope")) # Defaults for get if not present is None
```
> 25 <br/>
> 26 <br/>
> 'nope'

```python
print(len(d))
```
> 4

```python
print(d.items())
print(d.keys())
print(d.values())
```
> [('age', 26), ('height', 1.75), ('name', 'memo'), ('sex', 'male')] <br/>
> ['age', 'height', 'name', 'sex'] <br/>
> [26, 1.75, 'memo', 'male'] <br/>

##Strings 
Strings are immutable
```python
str(f)
```
> '42.42'

```python
s = "plop"
print(s[1])
print(s[0:3])
```
> l <br/>
> plo

```python
v1 = 42
print("Value of s: " + s + " . And v1: " + v1)
```
> TypeError: cannot concatenate 'str' and 'int' objects

```python
print("Value of s: " + s + " . And v1: " + str(v1))
```
> Value of s: plop . And v1: 42

```python
print("This is a string: %s and this an integer: %d" % (s, v1))
print("This is a string: %s and this an integer: %s" % (s, v1)) #Automatic str() with %s
```
> This is a string: plop and this an integer: 42 <br/>
> This is a string: plop and this an integer: 42

```python
print("Value of s: {} . And v1: {}".format(s, v1))  # Since python 2.7
print("Value of s: {0} . And v1: {1}".format(s, v1))
print("Value of v1: {1} . And s: {0} . And v1 again: {1}".format(s, v1))
print("plop {} " "plop".format(s))
```
> Value of s: plop . And v1: 42 <br/>
> Value of s: plop . And v1: 42 <br/>
> Value of v1: 42 . And s: plop . And v1 again: 42 <br/>
> plop plop plop

```python
print(s.capitalize())
print(s.upper())  # lower() also exists
```
> Plop <br/>
> PLOP

```python
print(s.count("p"))
print("pl" in s)
print(s.find('o')) # Returns index in the string
```
> 2 <br/>
> True <br/>
> 2

```python
print(s.encode(encoding='base64'))
a = s.encode(encoding='base64')
print(a.decode(encoding='base64'))
```
> plop <br/>
> cGxvcA==

```python
print(s.startswith('pl'))
print(s.endswith('dd'))
```
> True <br/>
> False

```python
print(len(s))
```
> 4

```python
print(s.replace('pl', 't'))
```
> top

```python
print("This_is_a_sentence".split("_"))
print(" ".join(['This', 'is', 'a', 'sentence']))
```
> ['This', 'is', 'a', 'sentence'] <br/>
> This is a sentence

```python
print("      This is a sentence       ".strip())
```
> This is a sentence

```python
s = 'Text'
s = "Text with 'quote'"
s = ''' Text '''
s = """Text """
```

```python
a = input("Please type your input: ") # Will expect quoting
print(a)
a = raw_input("Please type your input: ")
print(a)
```
> Please type your input: "sasasasas" <br/>
> sasasasas <br/>
> Please type your input: sasasasas <br/>
> sasasasas

##Bytes
- **! Python3 !**
- Bytes objects are immutable sequences of single bytes.
- Since many major binary protocols are based on the ASCII text encoding, bytes objects offer several methods that are only valid when working with ASCII compatible data.
- Only ASCII characters are permitted in bytes literals (regardless of the declared source code encoding). Any binary values over 127 must be entered into bytes literals using the appropriate escape sequence.
- Supports classic strings methods

```python
b'still allows embedded "double" quotes'
b"still allows embedded 'single' quotes".
b'''3 single quotes'''
b"""3 double quotes"""
```

```python
print(bytes.fromhex('2Ef0 F1f2  '))
print(b'\xf0\xf1\xf2'.hex())
```
> b'.\xf0\xf1\xf2' <br/>
> f0f1f2

Bytes objects behave like immutable sequences of integers
```python
b = b'Plop'
print(b[0])
```
> 80

##Bytearray
- **! Python3 !**
- Bytearray objects are a mutable counterpart to bytes objects.
- There is no dedicated literal syntax for bytearray objects, instead they are always created by calling the constructor bytearray()
- Supports classic strings methods

```python
bytearray(b'Hi!')
```

##Other Types
- **None**
```python
a = None
print(type(a))
```
> NoneType

- **Module**
```python
import sys
print(type(sys))
```
> module

- **Functions**
```python
def f():
    pass
print(type(f))
```
> function

- **Class's, Instances, Methods**
```python
class Plop():
    def __init__(self):
        pass:     
print(type(Plop))
print(type(Plop()))
print(type(Plop.__init__))
```
> instance <br/>
> classobj <br/>
> instancemethod

- **Types**
```python
print(type(type(1)))
```
> type

