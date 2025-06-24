# Without running this code, what will it print? Why?

dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

# It should print: [1, 42, 3]. Even though 'dict1' and 'dict2' are different objects, the 'dict'
# constructor created a shallow copy so the values are shared. Any mutations to 'dict1' would be 
# reflected in 'dict2'.
