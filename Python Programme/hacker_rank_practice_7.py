user_input = int(input("Enter a number:"))


def print_formatted(number):
    for i in range(1, number + 1):
        print('{0:>d} {0:>1o} {0:1X} {0:>1b}'.format(i))
        # format(i)
        # format(i, 'b')
        # format(i, 'o')
        # format(i, 'X')


for num in range(1, user_input + 1):
    width = len(str(num))
    for base in 'doXb':
        # print('{0:{width}{base}}'.format(num, base=base, width=width))
        print('{0:{width}{base}}'.format(num, width=width, base=base), end=' ')
    print()

print()
# print_formatted(user_input)
print('The value in decimal : %d' % user_input)
print('The value in octal: %o' % user_input)
print('The value in hex : %X' % user_input)
print('The value in hex : %x ' % user_input)
# print('The value in hex : %b ' % user_input)
# print(format(user_input, 'b'))
# print(format(user_input, 'o'))
# print(format(user_input, 'x'))
# print(format(user_input, 'X'))
print('This is a binary number:', bin(user_input))
print('This is octal number:', oct(user_input))
print('This is hexa decimal number:', hex(user_input))
