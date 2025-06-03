# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.1718)

# Should give an error. Two parameters are defined, but 3 arguments are given. 
# The actual error is: 'TypeError: foo() takes 2 positional arguments but 3 were given'.
