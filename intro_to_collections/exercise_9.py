my_list  = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# Given the above code, answer the following questions and explain your answers:

# 1. Are the lists assigned to 'my_list' and 'another_list' equal?
# 2. Are the lists assigned to 'my_list' and 'another_list' the same object?
# 3. Are the nested lists at index 3 of 'my_list' and 'another_list' equal?
# 4. Are the nested lists at index 3 of 'my_list' and 'another_list' the same object?

# DON'T WRITE ANY CODE FOR THIS EXERCISE.


# Answers:

# 1. Yes. Both lists are pointing to the same values.

# 2. No. Each object is represented individually for each list and the list constuctor creates a new
# object.

# 3. The nested lists are equal as they are both lists that contain the same elements.

# 4. The nested lists are the same object as the list contructor creates a shallow copy of the
# iterable passed as an argument. Only the reference to the nested list gets copied. 
