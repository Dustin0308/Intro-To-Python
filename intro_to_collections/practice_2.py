# Create a function that converts a list to a tuple and then to a set, and returns all three 
# collections.

def converts_to(input_list):
    tup_data = tuple(input_list)
    set_data = set(input_list)
    return (input_list, tup_data, set_data)

print(converts_to([1, 2, 3, 4]))

# ([1, 2, 3, 4], (1, 2, 3, 4), {1, 2, 3, 4})
