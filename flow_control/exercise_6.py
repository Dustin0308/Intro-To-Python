# Write a function that takes a string as an argument and returns an all-caps version of the string 
# when the string is longer than 10 characters. Otherwise, it should return the original string. 
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.



def len_of_str(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(len_of_str('Hello World'))        # HELLO WORLD
print(len_of_str('goodbye'))            # goodbye

# It is probably best to change the name of the function to something like 'caps_long' since the
# function is actually converting a string to all uppercase and doing much more than finding the 
# length of a string. * Just for future reference. * - Function naming lesson. 
