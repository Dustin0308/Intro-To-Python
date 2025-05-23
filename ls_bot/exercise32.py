# What's the difference between these two approaches for getting user input?

# Approach 1
# print("What's your name?")
# name = input()

# Approach 2
# name = input("What's your name? ")

# Approach 1 prints out 'What's your name' and then sets the variable 'name' to input with the
# question 'What's your name?' for the user to respond to on the next line.

# Approach 2 incorporates input without using print and asks the user 'What's your name?' and 
# provides a space for user input on the same line.  

# Both still require user input.

print('What\'s your name?')
name = input()

name = input('What\'s your name? ')

