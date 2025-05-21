# Create a variable 'my_dict' containing keys 'a' and 'b' with values 1 and 2. Then mutate the
# dictionary by changing the value of 'b' to 3. Create another variable new_dict and reassign
# 'my_dict' to it. 

my_dict = {
    'a': 1,
    'b': 2,
}
print(my_dict)

my_dict['b'] = 3
print(my_dict)

new_dict = my_dict
print(new_dict)
print(my_dict)
