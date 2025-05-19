# Write a program names 'greeter.py' that greets 'Victor' three times. Your program should use a 
# variable and not hard code the string value 'Victor' in each greeting. Here's an example run of
# the program: 

# python greeter.py
# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.


# Please refer to 'greeter.py' for the solution to this exercise. Here is the solution though.
# This solution is called f-string interpolation.

name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')

# Here is also a nother solution to the above exercise. (This solution uses string concatenation)

name = 'Victor'
print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')
