# Modify the 'age.py' program you wrote in Exercise 3 of the Input/Output chapter. The updated code 
# should use a 'for' loop to display the future ages.

# age = int(input('Please enter your age: '))
# print()

# print(f'You are {age} years old.')
# print(f'In 10 years, you will be {age + 10} years old.')
# print(f'In 20 years, you will be {age + 20} years old.')
# print(f'In 30 years, you will be {age + 30} years old.')
# print(f'In 40 years, you will be {age + 40} years old.')

age = int(input('Please enter your age: '))
print(f'You are {age} years old.')
print()

for future in range(10, 50, 10):   # Sets the future range of in: 10 years, 20 years, etc. Step of 10 years. Stops at 50 becasue 'age.py' went to 40 years.
    print(f'In {future} years, you will be {age + future} years old.')
