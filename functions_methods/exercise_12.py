# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# An error because no arguments were supplied to foo() and foo() needs atleast one argument. If the
# first parameter had a default value like the other 2, it would output their default values.

# The actual error is: TypeError: foo() missing 1 required postitional argument: 'first'.
