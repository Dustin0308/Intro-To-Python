# Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)


# Foo has 3 paramaters. The second and third parameters have default values of 3 and 2 respectively.
# Python should ignore those default values when invoking foo() with argruments and output
# the arguments instead. The output should be:

# 42
# 3.141592
# 2.718


# If we don't supply an argument for the second or third parameters, it will out their default
# values of 3 and 2, respectively. 
