# copy over your code from lab 1 to this file

def fibonacci(number):
    if number == 0:
        result = 0
    elif number == 1:
        result = 1
    else:
        series1, series2 = 0, 1
        for _ in range(2, number + 1):
            series1, series2 = series2, series1 + series2
        result = series2
    return result

def sum_to_goal(numbers, goal):
    seen = {}

    result = 0

    for num in numbers:
        difference = goal - num
        
        if difference in seen and result == 0:
            result = num * difference
        
        seen[num] = difference

    return result
