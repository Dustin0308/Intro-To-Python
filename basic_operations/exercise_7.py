# What will the following code do? Why?

# int('3.1415')

# Answer: It will give a ValueError becasue '3.1415' is a float, and is not a valid integer.

# To output the above integer correctly, we must convert the float into an int:

number = float('3.1415')
number = int(number)
print(number)
