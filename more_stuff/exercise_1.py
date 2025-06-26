# What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# It first sorts the dictionary keys in alpabetical order: Antonina, Chris, Clare, Karis, Karl, 
# Trevor. It is supposed to return index [1] in all uppercase letters. So it will print: CHRIS.
