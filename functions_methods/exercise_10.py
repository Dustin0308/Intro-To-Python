# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)


# foo() has 3 parameters with the second and third parameter with default values of 3 and 2
# respectively. Python will output:

# 42
# 3.141592
# 2 
# Because no argument was given for the third parameter when invoking foo(), it will output the
# function's default value for that parameter, which is 2.
