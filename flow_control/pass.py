# Creating a block in an 'if' statement that does nothing using the 'pass' statement.

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass # We don't care about 9
else:
    print('value is something else')

# Adding a comment to a 'pass' is good practice so future programmers understand why it is there.
