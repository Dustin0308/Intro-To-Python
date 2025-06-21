# Let's try another variation on the even/odd-numbers theme.

# We'll return to the simpler one-dimensional version of 'my_list'. In this problem, you should write 
# code that creates a new list with one element for each number in 'my_list'. If the original number 
# is an even, then the corresponding element in the new list should contain the string 'even'; 
# otherwise, the element should contain 'odd'.

# Expected Output:
# pretty-printed for clarity
# [
#     'odd', 'odd', 'even', 'odd',
#     'even', 'even', 'even', 'odd',
#     'odd', 'even', 'even'
# ]


my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

result = []
for number in my_list:
    if number % 2 == 0:
        result.append('even')
    else:
        result.append('odd')

print(result)     


# OR you could use a list comprehension

result = [ 'even' if number % 2 == 0 else 'odd'         # This is a tenery expression to choose between the two values.
           for number in my_list ]
print(result)



# OR you can use a helper function to determine whether we should add 'even' or 'odd' to the 
# new list.

def odd_or_even(number):                                # Lines 44 & 45 is a helper function.
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)                          # Lines 47 & 48 is a list comprehension.
           for number in my_list ]
print(result)
