# This exercise has bug in hackerrank website so we will select pypy3 .
"""element = int(input("How many elements you want to enter:"))
integer_list = map(int, input("Enter space separated number:").split())
integer_list = tuple(integer_list)
print(integer_list)
if element == len(tuple(integer_list)):
    print(hash(integer_list))
else:
    print("Please enter a same number of inputs that you passed above.")
"""
"""
text_case = int(input('Enter the number of text cases:'))
for i in range(text_case):
    try:
        a = input('enter first number:')
        b = input('enter second number:')
        print(int(a) / int(b))
    except ArithmeticError as error:
        print('Error Code: integer division or modulo by zero')
    except Exception as error:
        print('Error Code: ', error)
        print("Error type is :", type(error).__name__)
"""
# for _ in range(int(input())):
#     a, b = input().split()
#     try:
#         print(int(a) // int(b))
#     except Exception as e:
#         print('Error Code: ' + str(e))


for _ in range(int(input())):
    try:
        a, b = input().split()
        # a,b=map(int, input().split())
        print(int(a) // int(b))
    except Exception as e:
        print('Error code: ' + str(e))
        print('Error code: ', e)
