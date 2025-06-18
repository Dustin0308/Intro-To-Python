# Using 'dict.keys', 'dict.values', and 'dict.items' to get lists of the keys, values, and key/value
# pairs from a dictionary.

people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

print(people_phones.keys())             # dict_keys(['Chris', 'Pete', 'Clare'])

print(people_phones.values())           # dict_values(['111-2222', '333-4444', '555-6666'])

print(people_phones.items())            # dict_items([('Chirs', '111-2222'),
#                                                     ('Pete',  '333-4444'),
#                                                     ('Clare', '555-6666')
#                                         ])


# Changing the dictionary to show how the corresponding lists are updated immediately.

people_phones = {
    'Chris': '111-2222',
    'Pete':  '333-4444',
    'Clare': '555-6666',
}

keys = people_phones.keys()
values = people_phones.values()

print(keys)                             # dict_keys(['Chris', 'Pete', 'Clare'])                  
print(values)                           # dict_values(['111-2222', '333-4444', '555-6666'])

people_phones['Max'] = '123-4567'
people_phones['Pete'] = '345-6789'
del people_phones['Chris']

print(keys)                             # dict_keys(['Pete', 'Clare', 'Max'])
print(values)                           # dict_values(['345-6789', '555-6666', '123-4567'])
