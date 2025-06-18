# Using 'remove', 'pop', and 'clear' methods to remove elements from a mutable sequence

# 'seq.remove'

my_list = [2, 4, 6, 8, 10]

my_list.remove(8)                           # Remove number 8
print(my_list)                              # [2, 4, 6, 10]


# 'seq.pop'

my_list = [2, 4, 6, 8, 10]

print(my_list.pop(1))                       # Removes the element at index[1], which is 4.
print(my_list)                              # [2, 6, 8, 10]

print(my_list.pop())                        # No idex given, by default removes last element in sequence, which is 10.
print(my_list)                              # [2, 6, 8]


# 'seq.clear'

my_list = [2, 4, 6, 8, 10]

my_list.clear()                             # Removes all elements from a sequence, leaving it empty.
print(my_list)                              # []
