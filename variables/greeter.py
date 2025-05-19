# This is the solution to exercise 5: Write a program named 'greeter.py' that greets 'Victor' three 
# times. Your program should use a variable and not hard code the string value 'Victor' in each 
# greeting. 

# (This is known as f-string interpolation)

name = 'Victor'
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')

# This solution is also acceptable. (This is known as string concatenation)

name = 'Victor'
print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')
