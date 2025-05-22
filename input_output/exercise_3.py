# Write a program named age.py that asks the user to enter their age, then calculates and reports
# the future age 10, 20, 30, and 40 years from now. Here's the output for someone who is 27
# years old.

# How old are you? 27

# You are 27 years old. 
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# in 40 years, you will be 58 years old. 

age = input('Please enter your age: ')
age = int(age)
print()

print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# You can also do it this way:

age = int(input('Please enter your age: '))
print()
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# Or this way:

age = input('Please enter your age: ')
print()
print(f'You are {age} years old.')
print(f'In 10 years, you will be {int(age) + 10} years old.')
print(f'In 20 years, you will be {int(age) + 20} years old.')
print(f'In 30 years, you will be {int(age) + 30} years old.')
print(f'In 40 years, you will be {int(age) + 40} years old.')



# Note: This is also in the 'age.py' file. 
