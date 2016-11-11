##Problem
Have you ever found yourself writing this:
```python
data = [1,2,3,4,5,6,7,8,9]

odd_result = []
for i in data:
	if i % 2 == 0:
		odd_result.append(i)

formated = []
for entry in data:
	formated.append("Number: {}".format(entry))
```

##Solution
There is a better way to write this:
```python
data = [1,2,3,4,5,6,7,8,9]

odd_result = [i for i in data if i % 2 == 0]

formated = ["Number: {}".format(entry) for entry in data]
```

##Syntax
```
result = [ < what to put in the list > < iterable > < optional condition > ]
```

##Nested comprehensive list:
```python
result = [i for i in [j for j in range(1, 200) if j > 100 ] if i % 2 == 0]
```

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
result = [cell for row in matrix for cell in row]
print(result)
```
> [1, 2, 3, 4, 5, 6, 7, 8, 9]

```python
result = [[cell for cell in row] for row in matrix ]
```
> [1, 2, 3, 4, 5, 6, 7, 8, 9]

##Let's generate some data for performance testing:
```python
tags = ["test1", "test2", "test3"]
import random
import uuid
big_list = [{"id": i, "uuid": str(uuid.uuid4()), "tag": random.choice(tags)} for i in range(0,1000000)]  #10 million

print(big_list)
```
> [{'id': 0, 'tag': 'test2', 'uuid': 'd290ac0d-9c54-497f-9287-d80f5f74e1a4'}, <br/> 
>  {'id': 1, 'tag': 'test1', 'uuid': '56150efd-1c0b-455f-9bca-715d37610ddc'}, <br/>
>  {'id': 2, 'tag': 'test3', 'uuid': '5bf5c7e0-5665-4fb0-884b-d064f0e03f90'}, <br/>
>  {'id': 3, 'tag': 'test2', 'uuid': 'bf0c96b4-c133-43db-8d04-36c8b8931fdb'}, <br/>
>  {'id': 4, 'tag': 'test1', 'uuid': 'aa87b549-2334-42ae-b197-008b5df77277'}, <br/>
>  {'id': 5, 'tag': 'test1', 'uuid': 'b4afc38e-1f7e-467f-aaa6-f6831efb2c98'}, <br/>
> ........ <br/>
> ........]

##Performance testing:

- **Using a bare for**
```python
In [30]: %%time
    ...: result = []
    ...: for i in big_list:
    ...:     if i['tag'] == "test1":
    ...:         result.append(i)
    ...: 
```
> CPU times: user 1.57 s, sys: 53.3 ms, total: 1.62 s <br/>
> Wall time: 1.58 s


- **Using a comprehensive list**
```python
In [35]: %%time
    ...: result = [i for i in big_list if i['tag'] == "test1"]
    ...: 
```
> CPU times: user 1.29 s, sys: 40 ms, total: 1.33 s <br/>
> Wall time: 1.3 s


- **Careful to how you access distionaries**
```python
In [52]: %%time
    ...: t = "test1"
    ...: result = [i for i in big_list if i.get('tag', "") == t]
    ...: 
```
> CPU times: user 2.54 s, sys: 100 ms, total: 2.64 s <br/>
> Wall time: 2.54 s


- **Filter and function**
```python
In [59]: %%time
    ...: def f(i):
    ...:     if i['tag'] == "test1":
    ...:         return True
    ...:     else:
    ...:         return False
    ...: result = filter(f, big_list)
    ...: 
```
> CPU times: user 1.71 s, sys: 76.7 ms, total: 1.78 s <br/>
> Wall time: 1.73 s


- **Filter and lambda**
```python
In [42]: %%time
    ...: result = filter(lambda i:i['tag'] == "test1", big_list)
    ...: 
```
> CPU times: user 1.49 s, sys: 107 ms, total: 1.6 s <br/>
> Wall time: 1.53 s

##Sets and Dictionaries comprehension
- **Set comprehension**
```python
result = {i for i in [1,2,3,3,3]}
print(result)
```
> {1, 2, 3}

- **Dictionary comprehension**
```python
d = {"key1": "value1", "key2": "value2"}
inverted = {value: key for key, value in d.items()}
print(inverted)
```
> {'value1': 'key1', 'value2': 'key2'}

```python
list1 = ["aa", "bb", "cc"]
list2 = ["11", "22", "33"]
result = {key: value for key, value in zip(list1, list2)}
print(result)
```
> {'aa': '11', 'bb': '22', 'cc': '33'}

