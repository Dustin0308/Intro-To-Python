# Write some code to create a deep copy of the dict1 object and assign it to dict2. You should only 
# modify the code where indicated.

# You may modify this line

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = ??? # You may modify the `???` part
            # of this line

# All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])




import copy                                 # MODIFICATION MADE HERE!

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)                # MODIFICATION MADE HERE!

# All of these should print False
print(dict1         is dict2)               # False
print(dict1['a']    is dict2['a'])          # False
print(dict1['a'][0] is dict2['a'][0])       # False
print(dict1['a'][1] is dict2['a'][1])       # False
print(dict1['b']    is dict2['b'])          # False
print(dict1['b'][0] is dict2['b'][0])       # False
print(dict1['b'][1] is dict2['b'][1])       # False
 


# Launce School, in the solution, said this:

# All of these should print True

print(dict1['a'][0][0] is dict2['a'][0][0]) # True
print(dict1['a'][0][1] is dict2['a'][0][1]) # True
print(dict1['a'][1][0] is dict2['a'][1][0]) # True
print(dict1['a'][1][1] is dict2['a'][1][1]) # True
print(dict1['b'][0][0] is dict2['b'][0][0]) # True
print(dict1['b'][0][1] is dict2['b'][0][1]) # True
print(dict1['b'][1][0] is dict2['b'][1][0]) # True
print(dict1['b'][1][1] is dict2['b'][1][1]) # True
