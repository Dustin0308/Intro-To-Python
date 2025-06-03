# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# Give an error. Since the second parameter has a default value, the third parameter must also have
# a default value. 

# The actual error is: 'SyntaxError: parameter without a default follows parameter with a default.'
