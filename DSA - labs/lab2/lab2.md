# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	# total is initialized to 0, which will be used to store the sum of the squares.
	total=0; # 1

	# We have a for loop that iterates over a range of numbers from 0 to (number - 1). This loop variable i takes on values from 0 to (number - 1).
	for i in range(0,number): # n + 1
		# Inside the loop, x is calculated as (i + 1). This is done to start with x equal to 1 for the first iteration, 2 for the second, so on...
		x = (i+1) # 2n
		# For each value of x, x*x is computed, which is equivalent to squaring x.
		# The result of x*x is added to the total in each iteration of the loop.
		total+=(x*x) # 2n
	# total variable is returned at the end of the execution.
	return total # 1

	# Since the loop runs number times, and each iteration consists of constant time operations, the overall time complexity of the function is O(number).
	#T(n) = (1) + (n+1) + (2n) + (2n) + 1 = 5n+3
```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6

'''
In this expression, there are no loops and iterations. It's a mathematical formula that computes the result based on the input number. Moreoever, the expression involves a fixed number of arithmetic operations (multiplications, additions, and divisions), and the time it takes to compute the result remains constant.

Therefore, the time complexity of the function is constant, denoted as O(1). It means that the time required to execute the function does not depend on the size of the input number.

Above, when function2() gets called, return is used once, but there are 6 operations that occur in return statement and each occurs once.

-> So, count = 6 + 1 = 7, T(number) = constant. O(number) = constant.

'''

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp

'''
BUBBLE SORT ALGORITH:

The outer loop runs from 0 to len(list) - 2, so it iterates through the indices of the list.
The inner loop also runs from 0 to len(list) - 2 - i, i is the current iteration of the outer loop. This inner loop iterates through a decreasing portion of the list because, with each pass of the outer loop, the largest unsorted element "bubbles up" to the end of the list.

Inside the inner loop, there are constant time operations:
- if(list[j] > list[j + 1]) is a constant time operation.
- The three lines of code for swapping elements are also constant time.

In the worst case, when the list is in reverse order (the largest element is at the beginning), the inner loop will make a full pass for each element in the list. This results in approximately n * (n - 1) / 2 comparisons and swaps, where n is the length of the list.

Therefore, the time complexity of the bubble sort algorithm (and this function) is O(n^2) in the worst case.

So, the time complexity of function3(list) is O(n^2).
'''

```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1
	for i in range(1 to number):
		total=total*(i+1)
	return total

'''
total=1 #1
Above, operator '=' will only be used once per function call and hence, has a count of 1.

for i in range(1 to number): # (n-1) + 1
Above, value of 'i' changes in every iteration of loop from 1 to (n-1), both inclusive. Thus, value of 'i'
changes (n-1) number of times, so count for 'i' is (n-1).
range() gets called once per loop execution, to get values the loop must iterate through.
-> so, count = n

total=total*(i+1) # 3(n-1)
Above, operators '=','*','+' are used in every iteration of the loop.
so, count = 3(n-1)

return total # 1
A value will be returned in every function call and a return will happen only once.
-> so, count = 1.

T(n):
Total number of operations required to generate a return value:
T(n) = 1 + n + 3n - 3 + 1
T(n) = 4n - 1
-> therefore, O(n)
'''
```


## In class portion


### Group members
List the members of your group member below:

	* Name 
	* Dev Soni (Me)
	* Ruslan Gofman
	* Jack Martin
	* Sarah Haque

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Dev Soni (Me) | 5.659 | 0.003 |
| Jack Martin |  2.805 | 0.614 |
| Ruslan Gofman | 5.55 | 0.10 |
| Sarah Haque | 6.182 | 0.988 |

### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number | 0.003 | 0.988 | 0.985 |
|fibonacci | 2.805 | 6.182 | 3.377 |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

-> From my observations, I can say that the reasons for the fatest Fibonacci for Jack was that he used a recursive calls in the function, to recursively calculate the Fibonacci of the input, which is pretty fast, as compared to making a for loop for the same operation, which I used in the lab1, for the function. On the other hand, me and Ruslan had the fastest sum_to_number (pretty much around the same timings) timings cause we used comparitively for loops and had the if statements for logic execution, which pretty much takes less execution times as compared to for loops. However, Sarah and Jack used inner loops for the same operation, which would ultimately take larger time lapse, for the thing.


## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?

  -> Actually, me and Ruslan had pretty much the same approach for two functions and Jack and Sarah had their algorithms pretty much similar, so in order to point out differences in our approaches, me and Roslin had the faster sum_to_number cause we did not use inner loops for the process, which what Jack did for his approach, including inner loop means an extra execution step for the algorithm which increases the time for the execution, so Jack and Sarah had the slowest times on sum_to_number, However, Jack had fibonacci function faster than me and Ruslin, cause he used a recursin call in his function definition, which is a faster approach than using a loop for the fibonacci algorith.

2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  

  -> Since the fibonacci function has been finished pretty the same way, in terms of the usuage of same number of variables, there is no extra space resources, however, in sum_to_goal after seeing the variables -  difference; the range; seen (list variable), ultimately use a bit of extra space resource in the file


3. What sort of conclusions can you draw based on your observations?

  -> To conclude this, programmers can have different code approaches and may get the same result, it's just some algorithm takes longer time than usual, and some are quicker. It is important, however to make sure you are using the most efficient method.



