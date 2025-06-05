# What does this code output, and why?

def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([])

# Prints empty. When the 'is_list_emptpy' function is invoked with an empty list as it's argument,
# it is falsy becasue empty collections such as '[]' have built-in falsy values in Python. 
