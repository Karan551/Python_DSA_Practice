from array import *

# Que:1-> Give an array with some integer type values. Write a python script to
# sort an array values.
arr = array('i', [55, 22, 44, 121, 12, 11])
# convert an array to a sorted list.
arr_list = sorted(arr)
arr = array('i', arr_list)
# Que:2-> Give a list of heterogeneous elements.Write a python script to remove all non int values from the list.
"""
lst = ['HTML', 1001, 'CSS', 'hello', 55, 'Python', 55.33, 'JavaScript', 'React', 12, 15, 20, True, False]
print(lst)
lst = [element for element in lst if isinstance(element, int) and not (isinstance(element, bool))]
# print(lst)
# this is the second method to solve this question.
num_lst = [element for element in lst if type(element) == int]
print(num_lst)
"""
# Que:3-> Write a python script to calculate average of elements in the list.
"""
number_lst = [12, 80, 15, 45, 50, 20, 11]
average = sum(number_lst) / len(number_lst)
print("Average is :", average)
print("Average is :", round(average, 4))
"""
# Que:4-> Write a python script to create a list of first N prime numbers.
# user_input = int(input("How many prime number you want to append in list: "))

prime_lst = []

# Ye abhi fix karna hai.
"""
def prime_num():
    x = 2
    while True:
        num, a = 2, 2
        x += 1
        # a = 2
        while num < x:
            while a < num:
                if num % a == 0:
                    break
                a += 1
            else:
                print(num)
                return num
            num += 1

"""

# calling a function.
# print(prime_num())
# print('This is a prime list', prime_lst)


# print('This is non-prime list:', non_prime_lst)
"""
# ye abhi check karna hai.
def next_prime(num):
    x = 2  # first prime number
    num += 1
    for i in range(2, num + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            return i

"""
# user_choice = int(input("How many Prime Terms you want to print:"))
"""
count = 0
for i in range(1, 6):
    a, b = 2, 2
    while True:
        while b < a:
            if a % b == 0:
                break
            b += 1
        else:
            print('This is prime number:', a)
        a += 1
        # break
    # counter variable
"""

# Que:5->Write a python script to create a list of first N terms of a Fibonacci Series.
# user_choice = int(input("How many Fibonacci Terms you want to print:"))
# a, b = 0, 1
# count = 0
# print(a, b, end=' ')
# while count < user_choice - 2:
#     print(a + b, end=' ')
#     a, b = b, a + b
#     # counter variable
#     count += 1
