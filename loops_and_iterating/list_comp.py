# A transformative list comprehension

squares = [ number * number for number in range(5) ]
print(squares)





# Doing the same thing with an ordinary 'for loop'

squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)





# Here is a selection example

multiples_of_6 = [ number for number in range(20) 
                   if number % 6 == 0 ]             # Splitting comprehension over 2 lines aids in readability.
print(multiples_of_6)




# Combining selection and transformation. This code selects all of the even numbers in the 
# specified range and then returns a list of squares of the chosen numbers.

even_squares = [ number * number
                 for number in range(10)
                 if number % 2 == 0 ]
print(even_squares)





# Iterating over a dictionary with comprehension.
# Suppose we have a dict of cats. Using the cat names as keys; each name is associated with the
# cat's coat color. We want to create a lsit of names in uppercase. This is nearly identical to 
# using the 'dict.keys' method. The only difference is that the list comprehension returns an
# ordinary list, not a dictionary view object.

cats_colors = {
    'Tess':    'brown',
    'Leo':     'orange',
    'Fluffy':  'gray',
    'Ben':     'black',
    'Kat':     'orange',
}

names = [ name.upper() for name in cats_colors ]
print(names)



# Suppose we now want to limit the result list to just orange cats. We can accomplish that by 
# adding a selection to the comprehension

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange' ]
print(names)




# Using multiple selection criteria. Limiting the result to cats whose name begins with 'L'.

cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange'
          if name[0] == 'L' ]
print(names)                                # ['LEO']
