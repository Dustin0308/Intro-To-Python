# Without running this code, what will it print? Why?
# Don't worry about having an exact match for the output. The important part is to show something 
# that accurately represents set2.

set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)


# Should print: {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)} becasue 'set1' and 'set2'
# reference the same object (a set in this case) so changes made in 'set1' should reflect in 'set2',
# and vice versa. 


# Launch School's solution is the same as mine with this comment:
# This result demonstrates that set1 and set2 reference the same set: if we add an element to set1, 
# we'll see that element when we look at set2. The opposite is true, too: if we add something to 
# set2, we'll see it in set1.

# This code also demonstrates that assigning a variable to another variable doesn't create a new 
# object. Instead, Python copies a reference from the original variable (set1) into the target 
# variable (set2).
