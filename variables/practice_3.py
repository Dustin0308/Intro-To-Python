# Reassignment vs. Mutation

num = 3                     # assignment (initialization)
my_list = [1, 2, 3]         # assignment (initialization)
my_dict = {
    'a': 1,
    'b': 2,
}

print(num)
print(my_list)
print(my_dict)


num = 42                    # Reassignment
my_list[1] = 42             # Reassignment of element,
                            # my_list is mutated!
my_dict['b'] = 3            # Reassignment of dict pair
                            # my_dict is mutated!

print(num)
print(my_list)
print(my_dict)

# You can still reassign the variables
my_list = [2, 3, 4]         # Reassignment
my_dict = {'x': 0}          # Reassignment

print(num)
print(my_list)
print(my_dict)
