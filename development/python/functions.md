##Basic
```python
def plop():
    print("PLOP")
    
plop()
```
> PLOP

##Argument
```python
def plop(printme):
    print("PLOP: {}".format(printme))
    
plop("Test")
```
> PLOP: Test

##Keyword arguments
```python
def plop(printme1, printme2):
    print("PLOP: {} / {}".format(printme1, printme2))
    
plop("a", "b")
```
> PLOP: a / b

```python
plop(printme2="two", printme1="one")
```
> PLOP: one / two

##Default values
```python
def plop(printme1, printme2="two"):
    print("PLOP: {} / {}".format(printme1, printme2))
    
plop("a")
```
> PLOP: a / two

```python
plop("a", "b")
```
> PLOP: a / b

##Return
```python
def plop(printme1, printme2="two"):
    print("PLOP: {} / {}".format(printme1, printme2))
    
result = plop("a", "b")
print(result)
```
> PLOP: a / b
> None

```python
def plop(printme1, printme2="two"):
    text = "PLOP: {} / {}".format(printme1, printme2)
    return text
    
result = plop("a", "b")
print(result)
```
> PLOP: a / b
