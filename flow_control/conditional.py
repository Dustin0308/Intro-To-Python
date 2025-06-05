value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

# This is a nested 'if' statement and should be avoided as much as possible. When you have to use
# nested 'if' statements, keep the nesting to a modest 2 or 3 levels deep and use functions to
# isolate some of the more complex code. 

# The above code can be rewritten using an 'elif' block:

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')

# You can have as many 'elif' blocks as needed, buy they all need to be after the 'if' block and,
# if the code has one, before the 'else' block. The 'elif' conditionals are evaluated in the order
# they appear in the code.

# 'if' statement blocks may contain as many lines as you need:

if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    print('value is 9')
    print('value is an odd number')
    print('value is NOT a prime number')
else:
    print('value is something else')
