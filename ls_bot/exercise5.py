# What will the following code do and why? Don't run it until you have tried to answer. 

# colors = ['red', 'green', 'blue']         # a list colors with red, green, and blue.

# def change_colors():                      # defines a new color, 'yellow' at index[0], 'red'.
    # colors[0] = 'yellow'

# change_colors()                           # applies the change
# print(colors)                             # prints the new list ['yellow', 'green', 'blue']

colors = ['red', 'green', 'blue']

def change_colors():
    colors[0] = 'yellow'

change_colors()
print(colors)
