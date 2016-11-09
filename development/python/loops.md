##While
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
> 0 <br/> 
> 1  
> 2 
> 3 
> 4 

##For
```python
for i in range(0,12,2):
    print(i)
```
> 1
> 2
> 3
> 4
> 5

range([start], stop[, step])
- Start: Starting number of the sequence.
- Stop: Generate numbers up to, but not including this number.
- Step: Difference between each number in the sequence.

##Continue
```python
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        continue
    print(i)
```
> 1
> 2
> 4
> 5

##Break
```python
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    print(i)
```
> 1
> 2

##Pass
```python
for i in [1, 2, 3, 4, 5]:
    if i % 2 == 0:
        pass
    else:
        print(i)
```
> 1
> 3
> 5

##Try .. Except
```python
a = 5 /0
```
> ---------------------------------------------------------------------------
> ZeroDivisionError                         Traceback (most recent call last)
> <ipython-input-489-0aec5d0a819c> in <module>()
> ----> 1 a = 5 /0
> ZeroDivisionError: integer division or modulo by zero

```python
try:
    a = 5 / 0
except:
    print("error")
```
> error
