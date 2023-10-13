# Que:->Write a program to count the character in a string.
from string import whitespace, punctuation, hexdigits, ascii_letters

print(punctuation)
print(hexdigits)
print(ascii_letters)
user_string = '''Hello


hEllo
heLlo
 
hellO'''

count = 0
space = 0
new_line = 0
print(list(user_string))
for char in user_string:
    if char == ' ':
        space += 1
        print('this is a space.')
    elif char == '\n':
        print('This is a new line.')
        new_line += 1
    else:
        count += 1
print('Total character is:', count)

extra_space = ('\t', '\n', '\r', '\v', '\f', ' ')
count2 = 0
for char in user_string:
    if char not in extra_space:
        count2 += 1
print('Total characters is---', count2)

# print(user_string)
# print(len(user_string))
# print(count)
# print('This is a space:', space)
# print('This is a new Line:', new_line)
#  print(string.__all__)
