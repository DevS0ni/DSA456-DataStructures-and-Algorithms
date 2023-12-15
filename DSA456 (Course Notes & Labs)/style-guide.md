# Style Guide

Here is a style guide for you to follow:

## Documentation

Proper styling and documentation is important and makes a difference in how well your program reads. As you are training to be professionals, you should develop a proper styling for your programs. These are guidelines for this course.
Documentation

Proper documentation is about quality not quantity. Documenting every line of code is not useful. However, you need to provide good documentation. Here are some general do's and dont's for documentation


### DO's :

* **DO** state intentions

```python
# this function accepts an integer and calculate's the n'th fibonacci value
# in the fibonacci sequence.  it returns this number.
def fib(int n):		
```

* **DO** state things that go beyond names (like units):
```python
height = 50  # the height of the triangle in cm
```

* **DO** state for each function what it accepts, what it returns and what it does (at a high level), special cases, etc.
```python
# this function inserts a new node with data into the list before the node referred to by loc.
# function returns iterator to the newly inserted node.  
# loc is allowed be end()
def insert(loc, data): 
```

### Dont's:

  * **Don't** state the obvious
```python

x = 5             # x is an integer

# fib is a function, it accepts n
def fib(n):      
```

  * **Don't** write line by line comments that mirrors the code... documentation is about intention. You want to state why are you doing something instead of what you are doing. The what should be obvious from the code. The intention is not always obvious and needs documentation.

```python
for i in range(10):     # this is a for loop, it runs 10 times
  x = x+1               # add 1 to x
  y = y-1               # subtract 1 from y
```

## Style

  * Indentation: clear indentation isn't just about styling in python, it is makes or breaks your code.  
  * Use meaningful variable names:
     * don't use single letter variable names except for something like a loop counter.
     * don't use the variable name flag. This is as meaningless as x. especially bad if you have flag1, flag2, etc.
  * snake_case variable/function names is preferred.  This means put _ between every word.
```python
this_is_a_variable = 0
the_name = "a"
```
  * class names should capitalize every word
  * Tabs and Spacing
    * tab size: 2, 4 or 8? pick one... don't change it halfway through program
    * tabs vs spaces: pick one, stick with it. No matter what, make sure its correct and consistent.
    


Good styling is about consistency. However you choose to do the things that are not spelled out, is up to you. However, you need to be consistent within your own styling.


