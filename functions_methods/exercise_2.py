# Take a look at this code snippet:

foo = 'bar'     # global scope

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?

# The program should print 'bar' to the output because 'foo' is defined outside the scope of the
# function, specifically at global scope. Line 6 has 'foo = qux' but it's defined within the scope
# of the function. This 'foo' on line 6, shadows the 'foo' variable on line 3, so the line 6
# 'foo' does not change the value of the global scope 'foo' on line 3. If you wanted to print
# 'foo' on line 6, you would have to set 'print(foo)' within the function on line 7, keeping the
# same indentation so it remians in the scope of the function. The 'foo' on line 3 is assessable
# in the function if we were to comment out 'foo = qux' and set 'print(foo)' within the function
# it would print 'bar' twice as the function has access to the globally scoped 'foo' on line 3.
# Once you set 'foo = qux' within the function, the function cannot access the globally scoped
# 'foo' because 'foo' is redifined in the function itself. 
