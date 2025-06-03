# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# Since there is only one argument given when invoking foo(), the output will apply that argument
# to the first paramter, and the other 2 parameters have default values of 3 and 2, which will
# be their output. It will output the following: 

# 42
# 3
# 2
