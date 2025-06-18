# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse 
# order from the original. It should also exclude the first and last members of the original. The 
# result should be the tuple (4, 3, 2).

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)                    # Converted 'my_tup' to list: [1, 2, 3, 4, 5]
my_list.reverse()                           # Reversed 'my_list': [5, 4, 3, 2, 1]
result = tuple(my_list[1:4])                # Result converts 'my_list' to tuple at start:stop [1:4].
print(result)                               # (4, 3, 2)


# It can also be done these different ways. 

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[-2:-5:-1]                 # 5 is [-1], 4 is [-2], 3 is [-3], etc...
print(result)                               # (4, 3, 2)


# OR

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)                               # (4, 3, 2)
