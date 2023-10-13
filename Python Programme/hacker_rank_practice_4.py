# user_string = input('Enter your string:')
lst = ['isdigit()', 'isalnum()', 'isupper()', 'islower()']

# for i in user_string:
#     # if eval(f"{i},{lst[0]}"):
#     print(eval(f"{i}{lst[0]}"))

# print(eval(f"'a'{lst[0]}"))
# for i in lst:
#     for j in user_string:
#         print(eval(f"{j}.{i}"))
#         print(f'{j}')
# any(eval(f'c.{method}') for c in s)
# else:
# print(False)
"""
# This is the first optimal way to solve this question this is shortcut method.
methods = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
# this result via hackerRank community.
for method in methods:
    # this is a technique to solve this question
    if any(method(c) for c in user_string):
        print(True)
    else:
        print(False)
"""
# for c in user_string:
#     x = methods[2]
#     print(x(c))


# s = input()
'''
lis = ['isalnum()', 'isalpha()', 'isdigit()', 'islower()', 'isupper()']
for method in lis:
    result = any(eval(f'c.{method}') for c in user_string)
    # print(any(eval(method)))
    # this is a technique to solve the above approach.this returns generator so we
    # will have to convert an iterable to show the value.
    print(list(eval(f'c.{method}') for c in user_string))
    # print(result)
'''
# this another approach to solve the question
'''
s = input()
has_alnum = any(char.isalnum() for char in s)
has_alpha = any(char.isalpha() for char in s)
has_digit = any(char.isdigit() for char in s)
has_lower = any(char.islower() for char in s)
has_upper = any(char.isupper() for char in s)
print(has_alnum)
print(has_alpha)
print(has_digit)
print(has_lower)
print(has_upper)
'''
# this is just testing purpose.
a = 'hello'
width = 20
print(a.ljust(width, '-'))
print(a.rjust(width, '-'))
print(a.center(width, '-'))


# We can solve above question like this method, but it is not optimal method.
def check_is_alpha(string):
    for i in string:
        if i.isalpha():
            print(True)
            break
    else:
        print(False)


def check_is_digit(string):
    for i in string:
        if i.isdigit():
            print(True)
            break
    else:
        print(False)


def check_is_upper(string):
    for i in string:
        if i.isupper():
            print(True)
            break
    else:
        print(False)


def check_is_lower(string):
    for i in string:
        if i.islower():
            print(True)
            break
    else:
        print(False)

# call the function
# check_is_lower(user_string)
