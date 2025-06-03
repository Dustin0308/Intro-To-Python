# Without running the following code, what do you think it will do?

def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# Should give an error because 'foo' has two parameters and we only passed one argument. 
# The actual error is "TypeError: foo() missing 1 required postitional argument: 'qux'".
