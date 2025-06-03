# Write a function called 'format_name' that takes 'first_name' and 'last_name' as parameters with 
# default values of 'John' and 'Doe', and returns the full name.

def format_name(first_name='John', last_name='Doe'):
    return f'{first_name} {last_name}'

print(format_name())
