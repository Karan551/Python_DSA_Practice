#Que:1-> Write a python script to create a Arithmetic error.
a=9
b=0
#print(a/b)
#Que:2-> Write a python script to create a ValueError.
a=5
#Que:3-> Write a python script to handle the ArithmeticError.
'''a=7
try:
	b=int(input('Enter a number:'))
	c=a/b
except ArithmeticError:
	print('Cannnot divide By zero.')
except Exception:
	print('Invalid Input.')
else:
	print(f'{a} divide by {b} is = {c}')'''
#Que:4-> Write a python script to handle the ValueError.
'''a=5
try:
	b=int(input('Enter a number:'))
	if b==0:
		raise ValueError()
	c=a/b
except ValueError:
	print('Cannot be divided by Zero.')
except Exception:
	print('Invalid Input.')
else:
	print('Divide is =',c)'''	
#Que:5->Write a python script to handle multiple exception in one try.
'''a=4
try:
	b=int(input('Enter a number:'))
	c=a/b
except Exception:
	print("Invalid Input.")
else:
	print('Division is =',c)'''
#Que:6-> Write a python script to create a calculator with 4 basic operators and handle a maximum number of exceptions.
'''num_1=int(input('Enter a first number:'))
num_2=int(input('Enter a second number:'))
operator=input('What operator you want to perform(like: +, - , * , /):')
try:
	if operator== '+' or operator =='add':
		sum=num_1+num_2
		print('Sum is =',sum)
	elif operator== '-' or operator =='sub':
		sub=num_1-num_2
		print('Subtraction is =',sub)
	elif operator== '*' or operator =='multiply':
		multiply=num_1*num_2
		print('Multiplication is =',multiply)
	elif operator== '/' or operator =='divide':
		divide=num_1/num_2
		print('Division is =',divide)
	else:
		print('Invalid operator.')
except ZeroDivisionError:
	print('Cannot be divide by zero.')
except Exception:
	print('Please Enter a valid input.')
#Que:7-> Write a python script to add a finally block for the above script.
finally:
	print('Operation is performed.')'''
#Que:8->Write a python script to implement try and except and else block for division.
'''num_1=int(input("Enter first number:"))
try:
	num_2=int(input("Enter second number:"))
	result=num_1/num_2
except ZeroDivisionError:
	print("Cannot be divided by zero.")
except Exception:
	print('Please enter a valid input.')
else:
	print('Division is =',result)'''
#Que:9-> Write a python script to raise a ValueError.
a=9
try:
	b=input('Enter a number:')
	if b.isalpha():
		raise ValueError()
	b=int(b)
	c=a/b
except ValueError:
	print('Invalid value is given.')
except Exception:
	print('Invalid Input.')
else:
	print('Division is =',c)		