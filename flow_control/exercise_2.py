# Write a function, 'even_or_odd', that determines whether its argument is an even or odd number. If
# it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument
# is always an integer.

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

# This could also be written like this, which is a ternary expression ( I did not use this in my 
# origninal answer, I used the first code):

def even_or_odd(number):
    print('even' if number % 2 == 0 else 'odd')
