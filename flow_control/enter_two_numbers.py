# Create a program that asks the user to enter two numbers. Then use comparison operators to 
# determine and print whether:

# The first number is greater than the second
# The two numbers are equal
# The first number is less than the second

def enter_two_num(num1, num2):
    if num1 > num2:
        print(f'{num1} is greater than {num2}.')
    elif num1 == num2:
        print(f'{num1} is equal to {num2}.')
    else:
        print(f'{num1} is less than {num2}.')

user_input1 = input('Please enter your first number: ')
user_input2 = input('Please enter your second number: ')
user_num1 = float(user_input1)
user_num2 = float(user_input2)
enter_two_num(user_num1, user_num2)
