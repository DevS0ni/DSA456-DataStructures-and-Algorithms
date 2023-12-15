# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Soni Dev.
# Student Number: 130759210.
#

def wins_rock_scissors_paper(player_move, opponent_move):
    
	# This will help to handle the case sensitivity of the
	# arguments passed onto the function.
	player_move = player_move.lower()
	opponent_move = opponent_move.lower()

	# This variable will store the result of the stone, paper and scissors game.
	result = False

	# Selection conditions of a winner.
	if(player_move == 'rock' and opponent_move == 'scissors'):
		result = True
	elif(player_move == 'paper' and opponent_move == 'rock'):
		result = True
	elif(player_move == 'scissors' and opponent_move == 'paper'):
		result = True

	# returning the result.
	return result

def factorial(number):

	# 0! is defined as 1
    if number == 0:
        result = 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
    return result

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
    

class UpCounter:
    def __init__(self, step_size=1):
        self.step_size = step_size
        self.count_value = 0

    def count(self):
        return self.count_value

    def update(self):
        self.count_value += self.step_size



class DownCounter(UpCounter):
    def update(self):
        self.count_value -= self.step_size
