# What does the following code print?

# number1 = input('Enter a number: ')
# number2 = input('Enter a number: ')

# print(number1 + number2)

# It will concatenate both strings because the '+' operator does that when used in between two 
# strings. It will not add them. You must convert both to a float or integer first for them to add
# them correctly. Here is a proper example: 

number1 = float(input('Enter a number: '))
number2 = float(input('Enter a number: '))

print(number1 + number2)
