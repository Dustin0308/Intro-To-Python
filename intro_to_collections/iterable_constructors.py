# Lists, tuples, sets, and frozen sets share two common constructor forms:

# list() or list(iterable)
# tuple() or tuple(iterable)
# set() or set(iterable)
# frozenset() or frozenset(iterable)
# The constructors with no arguments create an empty list, tuple, set, or frozen set, as appropriate: a sequence or set with no members.

# The constructors that take an iterable argument expect an object that Python can iterate: 
# an iterable. From the built-in types, the iterables include all sequences, strings, sets, and 
# mappings. (Note that iterating a mapping iterates the mapping's keys.) Thus, you can use these 
# constructors to convert lists to tuples, tuples to sets, strings to lists, and so on:

my_str = 'Python'
print(my_str)

my_list = list(my_str)
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)

my_set = set(my_tuple)
print(my_set)


# Duplicating a collection
my_list = [5, 12, 2]
another_list = list(my_list)

print(my_list)
print(another_list)

print(my_list == another_list)
print(my_list is another_list)



# Involving Nested lists:

my_list = [[1, 2, 3], [4, 5, 6]]
another_list = list(my_list)

print(my_list)                          
print(another_list)                     

print(my_list == another_list)          
print(my_list is another_list)          
print(my_list[0] is another_list[0])    
print(my_list[1] is another_list[1])  




# Passing a string to any of these constructors causes it to iterate over the characters in the 
# string. It places each character in a separate element of the resulting collection:

print(tuple('Python'))
# ('P', 'y', 't', 'h', 'o', 'n')
