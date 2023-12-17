# Lab 3

This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.

## Objectives:

- learn to write recursive functions
- learn to analyze recursive functions

## Setup


All files needed for this lab were created by doing the first task in [lab 0](lab-00.md).  If you didn't do lab 0, do the first task to create your lab repository.


- All code is to be written in lab3.py
- All answers to non-coding questions and analysis is to be written in lab3.md

## Resources

You may find the following parts of the notes useful:
* [how to do an analysis in 5 steps](https://seneca-ictoer.github.io/data-structures-and-algorithms/B-Algorithms-Analysis/how-to-do-an-analysis)
* [how to do a recursive analysis](https://seneca-ictoer.github.io/data-structures-and-algorithms/C-Recursion/analysis-of-recursive-functions)

## Part A Recursive functions

- Write the following python functions **recursively**.
- A non-recursive solution that works will not be given credit (even if it passes testing)

### function 1:

This function is passed a number and returns(number)! = (number)(number-1)(number-2)...(3)(2)(1). By definition, 0! = 1

Only a recursive solution will be accepted!

```python
def factorial(number)
```

### function 2:

Write the **RECURIVE** function linear_search. linear_search() is passed a list of values and a key. If a matching key is found in the list, function returns index of where the key was found. If the key is not found, function returns -1.

NOTE: you are not allowed to use any of the built in list functions for this problem. The only function you are allowed to use is len()

```python
def linear_search(list, key)
```

HINT: you may need to write the actual recursive function with a different set of arguments to accomplish this task.

### function 3:

Write the **RECURIVE** function binary_search. binary_search() is passed a sorted list of values and a key. If a matching key is found in the list, function returns index of where the key was found. If the key is not found, function returns -1.

NOTE: you are not allowed to use any of the built in list functions for this problem. The only function you are allowed to use is len()

```python
def binary_search(list, key)
```

HINT: you may need to write the actual recursive function with a different set of arguments to accomplish this task.

## Part B Analysis

Perform an analysis of the following recursive functions.

### function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```

### function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```

### function 3 (optional challenge):

Analyze the following function with respect to number

```python
def function3(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		half = number // 2
		result = function3(value, half)
		if (number % 2 == 0):
			return result * result
		else:
			return value * result * result

```


## Part C Reflection

1. Describe how to a approach writing recursive functions, what steps do you take?

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 


## Submitting your lab

In order to get a mark for this lab, you must submit:

- a complete working solution for every function in part A.

Also, please make sure you follow the steps listed below for a full mark:

- Place the analysis part for this lab into the file lab3.md

When you are happy with the state of your files, submit a link to your repo's lab3 folder into blackboard.  

Note: Submission of a link to Blackboard is an indication that your lab is ready for grading in the current state.  Do not submit a link until you are ready to be graded.



## Lab Rubric:

| Criteria       | Poor - 0 mark     | Fair - 0.5 marks                                                                                                                     | Good - 1 marks                                                              |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Lab Completion | Part A not completed | Coding Completed, analysis/reflection is missing or poorly done | Successfully complete coding, analysis and reflection portions |
