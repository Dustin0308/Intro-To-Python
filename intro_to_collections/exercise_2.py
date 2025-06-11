# Can you write some code to change the value of 'bye' in the following tuples to 'goodbye'?

# stuff = ('hello', 'world', 'bye', 'now')


stuff = ('hello', 'world', 'bye', 'now')

# No. Tuples do not support item assignment as they are immutable. If it was, say a dict, you could 
# reference the index number associated with 'bye', which would be [2], and it would change it. But, 
# tuples cannot be mutated, you must create a new tuple. I have recreated an example of the above
# code to show the error that it outputs. 

stuff = ('hello', 'world', 'bye', 'now')
print(stuff)                                # ('hello', 'world', 'bye', 'now')
stuff[2] = 'goodbye'                        # 'stuff[2]' indexes the value at 2, which is 'bye'
print(stuff)                                # Output: TypeError: 'tuple' object does not support
                                            # item assignment.


# Launch School gave a solution I will include here by converting the orginal tuple to a list
# and set the element to the new value, then transform the list into a tuple, but it still
# creates an entirely new tuple. 

stuff = ('hello', 'world', 'bye', 'now')        # Tuple 'stuff' with values.
stuff = list(stuff)                             # Convert tuple to list. Lists are mutable.
stuff[2] = 'goodbye'                            # Set element at index 2 to 'goodbye'
stuff = tuple(stuff)                            # Convert list into tuple
print(stuff)                                    # ('hello', 'world', 'goodbye', 'now')
