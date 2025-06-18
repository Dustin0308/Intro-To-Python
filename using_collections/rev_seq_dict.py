# Reversing Sequences and Dictionaries

names = ('Grace', 'Clare', 'Allison', 'Trevor')
reversed_names = reversed(names)
print(reversed_names)                                       # reverse object at 0x76bcfc257cd0

print(tuple(reversed(names)))                               # ('Trevor', 'Allison', 'Clare', 'Grace'). Reversed tuple of names. 

print(names)                                                # ('Grace', 'Clare', 'Allison', 'Trevor'). Original 'names' unchanged. 



names = list(names)                                         # Converted 'names' to a list.
print(names.reverse())                                      # None. Reversed names, mutated. 
print(names)                                                # ['Trevor', 'Allsion', 'Clare', 'Grace']. The list was mutated and reversed.



my_dict = {'abc': 1, 'xyz': 23, 'pqr': 0, 'jkl': 5}
reversed_dict = reversed(my_dict)
print(reversed_dict)                                        # <dict.reversekeyiterator object at 0x76bcfbffddf0>



print(list(reversed_dict))                                  # ['jkl', 'pqr', 'xyz', 'abc']. Reversed dictionary keys.




# Iterating over a collection in reverse.

names = ('Grace', 'Clare', 'Allison', 'Trevor')
for name in reversed(names):
    print(name)
# Trevor
# Allsion
# Clare
# Grace
