##While
```python
i = 0
while i < 5:
    print(i)
    i += 1
```
> 0 <br/>
> 1 <br/>
> 2 <br/>
> 3 <br/>
> 4

##For
```python
for i in range(0,12,2):
    print(i)
```
> 0 <br/>
> 2 <br/>
> 4 <br/>
> 6 <br/>
> 8 <br/>
> 10

**range([start], stop[, step])**
- _Start_: Starting number of the sequence.
- _Stop_: Generate numbers up to, but not including this number.
- _Step_: Difference between each number in the sequence.

##Continue
```python
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        continue
    print(i)
```
> 1 <br/>
> 2 <br/>
> 4 <br/>
> 5

##Break
```python
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
    print(i)
```
> 1 <br/>
> 2

##Pass
```python
for i in [1, 2, 3, 4, 5]:
    if i % 2 == 0:
        pass
    else:
        print(i)
```
> 1 <br/>
> 3 <br/>
> 5

##Try .. Except
```python
a = 5 /0
```
> --------------------------------------------------------------------------- <br/>
> ZeroDivisionError                         Traceback (most recent call last) <br/>
> < ipython-input-489-0aec5d0a819c> in < module>() <br/>
> ----> 1 a = 5 /0 <br/>
> ZeroDivisionError: integer division or modulo by zero <br/>

```python
try:
    a = 5 / 0
except:
    print("error")
```
> error
