# Creat a file named 'personalized_greeting.py' with the following code:

# print("What's your name?")
# name = input()

# print(f'Good Morning, {name}!')

print("What's your name?")
name = input()

print(f'Good Morning, {name}!')

# You can also use the input() function to display the prompt the user sees:

name = input("What's your name? ")

print(f'Good Morning, {name}!')

# Note the space after the '?': the input() retrieved the input from the same line as the prompt,
# so the extra space separates your name from the end of the question being asked. 

# Without the space, we'd see:
# What's your name?Dustin
# Good Morning, Dustin!

# You can also have input() output a newline instead of a space:

name = input("What's your name?\n")

print(f'Good Morning, {name}!')

# In this code, the \n is an escape character that the computer treats as a newline. 
