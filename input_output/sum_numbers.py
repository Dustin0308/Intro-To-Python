# Write a program that asks for two numbers from the user, adds them, and then displays the result.

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = number1 + number2

print(f'The numbers {number1} and {number2} '
      f'add to {sum}')

# Entered the first number as 2 and the second number as 3. Got the result 23 which is incorrect.
# Number1 and number2 are strings so they must have a numeric type. Here's how:

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)

print(f'The numbers {number1} and {number2} add to {sum}')

# You can also use 'int' instead of 'float' in the above code.
