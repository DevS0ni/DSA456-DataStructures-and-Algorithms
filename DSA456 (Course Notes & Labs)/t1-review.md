## Q1:

What is the run time of the following function:

```python
def f1(number):
    rc = 1
    for i in range(0, 5):
        rc += 1
    return rc
```

```
Solution-1:

The run time of the function f1 = constant.
It has a fixed number of iterations (5) in the for loop, and the time complexity is O(1).
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

```
Solution-2:

The run time of the function f1 -> linear w.r.t n.
The loop runs until i becomes greater than or equal to n, and it increments i by 2 in each iteration.
Therefore, the time complexity is O(n).
```

## Q3:

Suppose that the function g1(n) has a run time of O(n) and g2(n) has a run time of O(n^2)  What is the run time of f1(n)?

```python
def f1(n):
    g1(n)
    g2(n)
```

```
Solution-3:

The run time of the function f1 would be the maximum of the run times of g1(n) and g2(n).
As in big-O notation, the time complexity would be O(max(O(n), O(n^2))), which simplifies
to O(n^2) since O(n^2) dominates O(n).
```

## Q4:

Write the following function recursively:

```python
def is_palindrome(word)
```
word is a character string.  This function returns true if word is a palindrome.  A palindrome is a string that reads the same forwards and backwards.  Thus:   noon, mom, dad are all palindromes.   table, texture, glass are not palindromes.

the above function can be a wrapper to a function that actually does the work

Try to write the function to O(n) run time where n is the length of s.

```python
# Solution-4:

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

# This implementation has a time complexity = O(n), where n is length of the string word.
```

## Q5:

When using a singly linked list to implement a stack, is it better for insertions to occur at the front or back of the list (or does it matter)?  Why?

```
Solution-5:

When using a singly linked list to implement a stack, insertions are typically better at the front of the list.
This is because inserting at the front takes constant time (O(1)) as you only need to update the head pointer,
while inserting at the back would require traversing the list to find the last node, resulting in a linear
time complexity (O(n)).
```

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

```
Solution-6(A):
[_, _, _, _, _, _, _, _, _, _]
```

#### part b
Insert the keys in the following order and show the final array:

* beta
* alpha
* gamma
* apple
* cherry
* orange

```
Solution-6(B):
[_, _, _, _, 'apple', 'cherry', 'beta', 'alpha', 'gamma', 'orange']
```

#### part c

remove apple from table in part b, what does final array look like

```
Solution-6(C):
[_, _, _, _, _, 'cherry', 'beta', 'alpha', 'gamma', 'orange']
```

#### part d

remove beta from table in part c, what does final array look like

```
Solution-6(D):
[_, _, _, _, _, 'cherry', _, 'alpha', 'gamma', 'orange']
```

#### part e

If you used tombstones in the previous parts, redo this question (parts A to D) without tombstones.  If you did it without tombstones, redo this question (parts A to D)  with tombstones 

```
Solution-6(E):
-- Without TombStones
[_, _, _, _, _, 'cherry', _, 'alpha', 'gamma', 'orange']

-- With TombStones
[_, _, _, _, 'tombstone', 'cherry', _, 'alpha', 'gamma', 'orange']
```

## Q7:

Describe what you will need to implement a queue using an array such that you have O(1) runtimes for enqueue() and dequeue() operations.  Do this WITHOUT using code (ie what do you need, why do you need it, but don't just code dump)

```
Solution-7:

For implementing a queue using an array with O(1) enqueue and dequeue operations,
you would need to use a circular array (circular buffer) and maintain two pointers:
one for the front and one for the back of the queue. This allows you to enqueue at
the back and dequeue from the front with constant time complexity.
```

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

```python
# Solution-8:

class SelfAdjustingList:
    def search(self, v):
        current = self.front

        while current is not None:
            if current.data == v:
                # Move the found node to the front
                # Adjust pointers accordingly
                # ...

                return True
            current = current.next

        return False
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

```
Solution-9:

The time complexity of the do_something function -> O(n), where n is the length of the string str.
Because, each recursive call processes one character of the string, and the function stops
when curr reaches the length of the string.

Each character is visited once, leading to a linear time complexity.
```
