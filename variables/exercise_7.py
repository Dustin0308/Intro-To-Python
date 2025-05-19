# What happens when you run the following code? Why?

# NAME = 'Victor'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# NAME = 'Nina'
# print('Good Morning, ' + NAME)
# print('Good Afternoon, ' + NAME)
# print('Good Evening, ' + NAME)

# The program will greet Victor 3 times and then greet Nina 3 times. Name should not be all caps
# because all caps is reserved for constants. Constants should not change and they do in this 
# example program, which is improper for Python even though Python allows it to be changed. 
# 'NAME' should be changed to 'name' to follow the proper naming conventions for variables. 
# I will write the proper code below.

name = 'Victor'
print('Godd Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)

name = 'Nina'
print('Good Morning, ' + name)
print('Good Afternoon, ' + name)
print('Good Evening, ' + name)
