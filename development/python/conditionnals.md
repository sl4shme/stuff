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
```python
if "false":
    print("test")
```
> test

```python
if "":
    print("test")
```
>

```python
if 1:
    print("test")
```
> test

```python
if 0:
    print("test")
```
>

```python
if [1,2,3]:
    print("test")
```
> test

```python
if []:
    print("test")
```
>

```python
if None
    print("test")
```
>

##And / or
```python
if (1 == 1) and False:
    print("plop")
```
>

```python
if (1 == 1) or False:
    print("plop")
```
> plop
