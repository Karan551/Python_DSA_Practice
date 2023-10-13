def odd_num(n):
    if n % 2 != 0 and n > 0:
        return n


dash = '-'
bar = '|'
period = '.'
num = int(input("Enter the door size:"))
# check that number is odd or not.
n = odd_num(num)
m = n * 3
num_dash = (m - 7) // 2
msg = 'welcome'
upper_half = (n - 1) // 2
print(upper_half)

# This is upper section.
count = 1
for i in range(upper_half, 0, -1):
    print(dash * (4 * i - i) + period * count)
    count += 2


# This is the middle section.(this is done)


def pattern(a, message='welcome'):
    """
    This function is used to print middle section of the door mate pattern.
    :param a:
    :param message:
    :return:None
    """

    def dash():
        for i in range(1):
            print('-' * a, end='')

    # calling the inner function.
    dash()
    # print msg
    print(message.upper(), end='')
    # calling inner function again.
    dash()

# this is the bottom section.
# calling the function.
# pattern(num_dash, msg)
