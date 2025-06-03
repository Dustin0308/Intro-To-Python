# Write a function called 'combine_words' that takes two parameters: 'word1' and 'word2' with a 
# default value of an empty for 'word2'. The function should return the two words combined with a
# hypehn between them. If 'word2' is not provided, it should return 'word1'.

# Example: 
# combine_words('super', 'hero')            # should return 'super-hero'


def combine_words(word1, word2=''):
    return word1 + '-' + word2

word1 = input('Enter your first word: ')
word2 = input('Enter your second word: ')
combined = combine_words(word1, word2)
print(combined)

# I have the correct solution in this exercise. Without learning flow control yet, the hypehn 
# remains if the user doesn't input the second word. It requires conditional logic 
# (which is taught in the next lesson) to remove the hypen in that use case. 
