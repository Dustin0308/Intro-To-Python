# Write a function called 'greet_user' that takes a name parameter with a deafault value of 'friend'
# and prints a greeting message that includes the name. 

# Example output with argument.
# greet_user('Dustin')           # Hello, Dustin! Welcome to Python programming.

# Example output without argument:
# greet_user()                   # Hello, friend! Welcome to Python programming. 

# My intitial answer, which isn't quite right even though it gives a similar output. 

# def greet_user():
#    name = 'friend' 
#    print(f'Hello, {name}! Welcome to Python programming.')

# greet_user()

# LSBot's solution/suggestion. 

def greet_user(name='friend'):
    print(f'Hello, {name}! Welcome to Python programming.')

greet_user()
greet_user('Dustin')

