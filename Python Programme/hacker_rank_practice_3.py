# a = 'hello'
# print(a.upper())
# print(a.lower())
# print('wOrLd', 'wOrLd'.swapcase())
# print(a.title())

# user_input = input("Enter the value that you want to convert:\n")


def swap_case(s):
    return s.swapcase()


def split_and_join(line):
    # write your code here
    line_list = line.split(" ")
    return '-'.join(line_list)


def print_full_name(first, last):
    # Write your code here
    return f'Hello {first} {last}! You just delved into python.'


def mutate_string(string, position, character):
    # This is first method to change character in a string.
    # (string -> list(and change) -> string(converting list into string) )
    """lst = list(string)
    lst[position] = character
    return ''.join(lst)
    """
    # This is the second method using slice method.
    new_string = string[:position] + character + string[position + 1:]
    return new_string


string1 = 'ABCDCDC'


# count = 0


# Que:Write a program to find a substring in a string to all occurrences.
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:len(sub_string) + i] == sub_string:
            count += 1
    return count


# def count(s):


# for i, ch in enumerate(string):
#     # Here we can add i+(n) where n is length our substring.
#     if 'CDC' == string[i:i + 3]:
#         count += 1
#     print(string[i:i + 3])
# print(f'\'CDC\' Number of times:', count)

# result = mutate_string(user_input, int(input()), input())

# print(result)
