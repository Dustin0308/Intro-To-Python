# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
print(foo)


# We get NameError: name 'foo' is not defined. Since 'foo' is created inside the function, 
# running code outside of that function means 'foo' isn't in scope because 'foo' is part 
# of the 'set_foo()' function. 'foo' is only assessble inside that function. 'foo' would have to
# be assigned a value in the top scope to print(foo).
