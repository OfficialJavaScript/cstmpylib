## Installation:
<br>
Make sure that the programs are in the same directory, then import it using:
<br><br>

```import randomstring```

## Usage:
```randomstring.<function>(<character count>)```
<br><br>
  
### Functions:
```‎letterstr‎()``` - This will generate a string made out of only lowercase and uppercase characters***
<br><br>
```numberstr()``` - This will generate a string made out of only numbers.
<br><br>
```abcspecialcharstr()``` - This will generate a string made out of only lower and uppercase characters and special characters,
<br><br>
```randomstr()``` - This will generate a string made out of lower and uppercase character, numbers and special characters.

### Examples:
main.py:
<br>
```
import randomstring

print(randomstring.letterstr(15))

```
Terminal:
```
ubuntu@ubuntu:~$ python3 main.py
toPZiUFEbbwryPk
```

<br><br>

main2.py:
<br>
```
import randomstring

print(randomstring.randomstr(20))

```
Terminal:
```
ubuntu@ubuntu:~$ python3 main2.py
V^T/ejs7M8&Ti{N45/1H
```
<br>

### Directory example:
```
ubuntu@ubuntu:~/folder$ ls
main.py  main2.py  randomstring.py
```
