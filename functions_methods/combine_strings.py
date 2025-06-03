# Create a function called 'combine_strings' that takes two parameters: 'first_string' and
# 'second_string'. The function should return the two strings concatenated together with a 
# space between them. Make second_string optional with a default value of an empty string.

# Example: 

# combine_string('Hello', 'World')          # should return 'Hello World'
# combine_string('Python')                  # should return 'Python'



def combine_strings(first_string, second_string=''):
    one_string = first_string + ' ' + second_string
    return one_string

first_string = input('Please enter your first string: ')
second_string = input('Please enter your second string: ')
result = combine_strings(first_string, second_string)
print(result)

