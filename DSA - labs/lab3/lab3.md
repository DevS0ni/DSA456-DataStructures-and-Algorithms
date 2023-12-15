# Analysis and Reflection for Lab 1

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0): #1
		return 1 #1 (only when condition is true)
	elif (number == 1): #1
		return value #1 (only when condition is true)
	else:
		return value * function1(value, number-1) # 1 + 1 + 1 + T(number - 1)
```

```
Let 'number' be the input/parameter to function1(), wherein value^number is calculated using recursion.
For analysis, let n = number
Let T(n) represent the total number of operations required to generate a return value.

When (number == 0), 2 ops
when (number == 1), 2 ops
when n >= 2, 5 + T(n-1)
i.e. T(n) = 5 + T(n-1), T(0) = 2, T(1) = 2

T(n) = 5+T(n-1)

T(n-1) will be evaluated as T(n-1)+T(n-2)+ _ _ _ + T(n-(n-2))+T(n-(n-1))+T(n-(n))

So, till T(n-(n-2)) 5 will be added and we have values for T(1) and T(0)

T(n) = 5+5(n-2)+4
T(n) = 5(n-1)+4
T(n) = 5n-1

T(n) = 5n - 1

∴ T(n) is O(n)
```

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b): # b = len(mystring)-1 = n-1
	if(a >= b ): #1
		return True # 1 (only when condition is true)
	else:
		if(mystring[a] != mystring[b]): #1
			return False # 1 (only when condition is true)
		else:
			return recursive_function2(mystring,a+1,b-1) # 1 + 1 + 1 + T(n - 3) # this return statement will be called b-2 time and b = n-1

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1) # 1 + 1

```

```
The order of growth of function2 will be equal to the order of growth of recursive_function2 because function2 is simply returning the result of recursive_function2.

Let mystring be the input/parameter to function2
Let n = len(mystring)
Order of growth of function2 = order of growth of recursive_function2

Let T(n) = total number of operations required to generate a return value of recursive_function2
T(n) = 5 + T(n-3)

When n = 3, true is returned by recursive_function2, lets say T(0) = 1, since true = 1, false = 0
T(n) = 5 + 5(n/3) + T(0)
T(n) = 5 + 5(n/3) + 1
T(n) = (5n + 18)/3
Therefore, T(n) is O(n)
Hence, function2 has order of growth of it's run-time as O(n)
```

### function 3 (optional challenge):

Analyze the following function with respect to number

```
This function calculates value^number
Let n = number
Let T(n) = number of operations equired to generate the return value
```

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

```
we have, T(0) = 2, T(1) = 3
When number is odd, there will only be one additional operator '+1', but that won't make a difference in asymptotic analysis because constants are ignored at large values of variable.
T(n) = 5 + T(n/2) + 4
T(n) = 9 + T(n/2)
T(n) = 9 + 9log(n)
At large values of n, (+9) and (*9) will become insignificant.
T(n) = log(n)
Hence, the order of growth of function3 is O(logn).
```

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?

-> For writing a recursive function, a base case must be setup that would terminate the process of recursive instance calling. It should be checked very cautiously that the base case is reached. Space and time complexity must also be considered so that the function can be optimized.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same?
   
-> In both recursive and non-recursive analysis, the constants are ignored at the end. In recursive analysis, it is important to consider how the function is broken down into smaller inputs and how the recurrence relation is applied.
