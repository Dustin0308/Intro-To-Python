# Using Unicode and actually referencing a single character:

# Ex. 1: Shows how 'letters[2]' returns the object at index 2 of the 'letters' list. Both 'char' and
# 'letters[2]' referencs the same object, as show on line 7.

letters = ['a', 'b', 'θ', 'd', 'e']
char = letters[2]
print(char is letters[2])
# Prints: True

# Ex. 2: This shows the two characters are not the same value but are distinct objects.

letters = 'abθde'
char = letters[2]
print(char is letters[2])
# Prints: Fasle





# *Note* - If you comment out lines 8 and 15, and add in the code 'print(char)', they both print
# out 'θ'. 
