#
# Author: Dev Soni
# Student Number: 130759210
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
    if (number == 0):
        return 1
    return (number * factorial(number-1))

# ---------------------------------------------------
# tail-recursive function: It will use less memory
# time complexity : Θ(n)
# space complexity : Θ(1)
# def factorial(number,result = 1):
#     if(number == 0):
#         return result
#     return factorial(number -1,result * number)
# ---------------------------------------------------

# Time complexity : O(n) , n = number of elements in the list
# Space complexity : O(n)
def linear_search(list, key, index=0):
    len_of_list = (len(list) - 1)
    if (list[index] == key):
        return index
    if ((index == len_of_list) and (list[index] != key)):
        return -1
    return linear_search(list, key, index+1)


# None will help in intialising high_index for the first time.
# time complexity : O(log n), n = number of elements in the list
# space complexity : O(log n)
def binary_search(list, key, low_index=0, high_index=None):
    if (high_index == None):
        high_index = (len(list) - 1)

    mid_index = ((low_index + high_index) // 2)

    if (low_index > high_index):
        return -1

    if (list[mid_index] == key):
        return mid_index
    elif (key > list[mid_index]):
        return binary_search(list, key, (mid_index+1), high_index)
    else:
        return binary_search(list, key, low_index, (mid_index-1))
