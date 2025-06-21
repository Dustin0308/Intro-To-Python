# Using 'for' loops with other collections, such as dicts.

# Looping over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key)




# If you want the values or pairs, you can request them with the 'values' or 'items' methods

# Looping over a dictionary's values
my_dict = {'a': 1, 'b': 2, 'c': 3}
for value in my_dict.values():
    print(value)


# Looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
    print(item)



# A more Pythonic way to iterate over both the keys and values simultaneously using tuple unpacking
my_dict = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in my_dict.items():             # This can be done without '()': for key, value in my_dict.items()
    print(f'{key} = {value}')
