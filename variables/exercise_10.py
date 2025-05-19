# Assume that 'obj' already has a value of '42' when the code below starts running. Which of the 
# subsequent statements reassign the variable? Which statements mutate the value of the object
# that 'obj' references? Which statements do neither? If necessary, you can read the documentation.

# obj = 'ABcd'                  # Reassignment. Changes 'obj' with a value of '42' to 'ABcd'.
# obj.upper()                   # Neither. This string is empty, does nothing. Obj is still obj = ABcd. 
# obj = obj.lower()             # Reassignment. obj = ABcd becomes obj = abcd.
# print(len(obj))               # Neither. Prints the length of obj = abcd which is 4.
# obj = list(ojb)               # Reassignment. Sets a new value for obj to obj = ['a', 'b', 'c'], which is a list.  
# obj.pop()                     # Mutation. Removes the last element of the list, 'd'. Obj now is obj = ['a', 'b', 'c'].
# obj[2] = 'X'                  # Mutation. Reassigns the element at index 2 to 'X', but still mutates the list as whole by changing the element within the existing list.
# obj.sort()                    # Mutation. Performs an in-place sort, which is a mutation. Sorts the elements in the list from least to greatest. Obj is now obj = ['X', 'a', 'b'].
# set(obj)                      # Neither. Shows obj as a set, but obj is still obj = ['X', 'a', 'b'] when printed.
# obj = tuple(obj)              # Reassignment. Reassigns the value of obj to a tuple. Obj is now obj = ('X', 'a', 'b').
