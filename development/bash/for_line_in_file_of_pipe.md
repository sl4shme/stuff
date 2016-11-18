## For line in file
```bash
while read line 
do
    echo $line
done < file.txt
```

## For line in piped entry
```bash
cat file.txt | while read -r line 
do
    echo $line
done
```

## Limitations of pipes
Because of the pipe, the while loop is executed in a subshell that has its own
environment.
```bash
counter=0
cat file.txt | while read -r line 
do
    counter=$(( $counter + 1))
done
echo $counter
```
> 0

## Solution
```bash
counter=0
while read -r line 
do
    counter=$(( $counter + 1))
done < <(cat file.txt)
echo $counter
```
> 3

or

```bash
counter=0
while read -r line 
do
    counter=$(( $counter + 1))
done <<< `cat file.txt`
echo $counter
```
> 3
