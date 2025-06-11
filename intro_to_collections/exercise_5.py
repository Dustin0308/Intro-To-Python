# How do the set types differ from the sequence types?

# 1. Set types maintain an UNORDERED collection of objects; Sequence types maintain an ORDERED 
# collection of objects.
# 2. Set types CANNOT have duplicates; Sequence types CAN have duplicates. 

my_set = {'a', 'b', 'c', 'c', 'd'} 
my_list = ['a', 'b', 'c', 'c', 'd']
print(my_set)                           # {'a', 'd', 'c', 'b'}. Unordered and removes duplicates.
print(my_list)                          # ['a', 'b', 'c', 'c', 'd']. Ordered and doesn't remove 
                                        # duplicates.

# 3. Set types CANNOT be indexed; Sequence types CAN be indexed. 

my_set = {'a', 'b', 'c', 'c', 'd'}
my_list = ['a', 'b', 'c', 'c', 'd']
print(my_list[2])                       # c. Sequences do support indexing. They are ordered.
print(my_set[2])                        # TypeError: 'set' oject is not subscriptable. In other 
                                        # words, it does not support indexing because it is unordered.
