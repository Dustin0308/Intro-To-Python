# Using key-based access with dicts

my_dict = {
    'a': 'abc',                        # string
    37: 'def',                         # integer
    (5, 6, 7): 'ghi',                  # tuple
    frozenset([1, 2]): 'jkl'           # frozen set
}

print(my_dict['a'])                     # abc
print(my_dict[37])                      # def
print(my_dict[(5, 6, 7)])               # ghi
print(my_dict[frozenset([1, 2,])])      # jkl
# print(my_dict['nothing'])               # KeyError: 'nothing'

# The 'dict.get' method returns the value associated with a given key if the key exits.

my_dict = {
    'a': 'abc',                        # string
    37: 'def',                         # integer
    (5, 6, 7): 'ghi',                  # tuple
    frozenset([1, 2]): 'jkl'           # frozen set
}

print(my_dict.get('a'))                # abc
print(my_dict.get('nothing'))          # None
print(my_dict.get('nothing', 'N/A'))   # N/A
print(my_dict.get('nothing', 100))     # 100

# Using key-based access to the left of the '=' operator

my_dict = {
    'a': 'abc',                        # string
    37: 'def',                         # integer
    (5, 6, 7): 'ghi',                  # tuple
    frozenset([1, 2]): 'jkl'           # frozen set
}

my_dict['a'] = 'ABC'
my_dict[37] = 'DEF'
my_dict[(5, 6, 7)] = 'GHI'
my_dict[frozenset([1, 2])] = 'JKL'
print(my_dict)                          # {'a': 'ABC', 37: 'DEF', (5, 6, 7): 'GHI', frozenset({1, 2}): 'JKL'}


# Assigning new keys to a dict

my_dict['xyz'] = 'Hey there!'
print(my_dict['xyz'])                   # Hey there!
