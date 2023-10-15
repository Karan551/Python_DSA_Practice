# Que:1-> Write a program to check that given number is prime or not using for loop.
user_num = int(input("Enter a number that you want to check: "))


def isPrime(num: int):
    """
    This function is used to check given number is Prime or not.
    :param num: int
    :return: str
    """
    for i in range(2, num):
        if num % i == 0:
            return f'{num} is not a Prime Number.'
    else:
        return f'{num} is a Prime Number.'


# Que:2-> Write a program to check that given number is prime or not using while loop.
def isPrime_while(num: int):
    """
    This function is used to check that given number is Prime number or not.
    :param num:
    :return:->str
    """
    # counter variable.
    count = 2
    while count < num:
        if num % count == 0:
            return f'{num} is not a Prime Number.'
        count += 1
    else:
        return f'{num} is a Prime Number.'


# Que:3-> Write a program to find Prime number between 1 to N.(using for loop).
def findPrime(num: int):
    """
    This function is used to find Prime Numbers between 1 to N.
    :param num:int
    :return:->None
    """
    count = 0
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(f'{i} ,', end=' ')
            count += 1
    print(f'\nThere are {count} Prime Numbers between 1 to {num}.')

# Que:4-> Write a program to find Prime number between 1 to N.(using while loop).


# calling a function
# result = findPrime(user_num)
