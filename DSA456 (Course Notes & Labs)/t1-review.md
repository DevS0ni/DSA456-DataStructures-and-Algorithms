## Q1:

What is the run time of the following function:

```python
def f1(number):
    rc = 1
    for i in range(0, 5):
        rc += 1
    return rc
```


## Q2:

What is the run time of the following function:

```python
def f1(n):
    rc = 1
    i = 0
    while i < n:
        rc += 1
        i += 2
    return rc
```

## Q3:

Suppose that the function g1(n) has a run time of O(n) and g2(n) has a run time of O(n^2)  What is the run time of f1(n)?

```python
def f1(n):
    g1(n)
    g2(n)
```

## Q4:

Write the following function recursively:

```python
def is_palindrome(word)
```
word is a character string.  This function returns true if word is a palindrome.  A palindrome is a string that reads the same forwards and backwards.  Thus:   noon, mom, dad are all palindromes.   table, texture, glass are not palindromes.

the above function can be a wrapper to a function that actually does the work

Try to write the function to O(n) run time where n is the length of s.


## Q5:

When using a singly linked list to implement a stack, is it better for insertions to occur at the front or back of the list (or does it matter)?  Why?


## Q6:

The following show a table of keys and the hash index of these keys within a table of size 10

| key | hashIdx |
|---|---|
| alpha | 8|
| beta | 9|
| gamma | 8|
| apple | 4 |
| orange | 4 | 
| cherry | 5 |


#### part a

Draw an empty array of size 10 that represents a linear probing table.

#### part b
Insert the keys in the following order and show the final array:

* beta
* alpha
* gamma
* apple
* cherry
* orange


#### part c

remove apple from table in part b, what does final array look like

#### part d

remove beta from table in part c, what does final array look like

#### part e

If you used tombstones in the previous parts, redo this question (parts A to D) without tombstones.  If you did it without tombstones, redo this question (parts A to D)  with tombstones 

## Q7:

Describe what you will need to implement a queue using an array such that you have O(1) runtimes for enqueue() and dequeue() operations.  Do this WITHOUT using code (ie what do you need, why do you need it, but don't just code dump)

## Q8:

A self adjusting linked list is a linked list where a successful search causes the list to adjust so that the found item is moved to the front (and thus allowing successive search for same item to be more readily found).
 
Given the following class declarations for a doubly linked self adjusting linked list:
 
```python
class SelfAdjustingList:
	class Node:
		def __init__(self, dat, nx, pr):
			self.data = dat
			self.next = nx
			self.prev = pr

	def __init__(self, id_list):
                self.front = ...
                self.back = ...
```

Write the following function:
```python 
def search(self, v)
```

* This function searches for v within the list and returns true if v is found.  If not found, function returns false
* The list will be adjusted so that the found node is moved so that it becomes the first data node in the list
* Function must have run time of O(n)
* Implement two versions of this, one using sentinels and one without.

## Q9: Recursive Analysis:

Perform an analysis on do_something() function with respect to the length of the string str
```python
def do_recursion(str, curr):
    if curr == len(str):
        return 0
    elif str[curr] == "a":
        return 1 + do_recursion(str, curr + 1)
    else:
        return do_recursion(str, curr + 1)

def do_something(str):
    return do_recursion(str, 0)
```

