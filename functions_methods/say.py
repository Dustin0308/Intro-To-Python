# Creating Functions

def say():
    print('Output from say')

print('First')
say()
print('Last')

# On line 7, the code 'say()' is a function call to the say function. When Python runs this 
# program, it creates a function named 'say' whose body causes Python to print the text:
# 'Output from say' when the functions executes, though it doesn't happen immediately.
# Python prints 'First' first, then jumps into the body of the function 'say', which prints
# 'Output from say', then Python returns to the code that immediately follows the call to 'say'
# and prints 'Last'.
