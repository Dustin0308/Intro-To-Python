# Letter case using 'str.capitalize', 'str.title', and 'str.swapcase'.

# 'str.capitalize'
print("what's up?".capitalize())                        # What's up? First letter of str capitalized. Everythin else lowercase.
print('456ABC'.capitalize())                            # 456abc. First letter of str capitalized. Everythin else lowercase.



# 'str.title'
print("four SCORE and sEvEn".title())                   # Four Score And Seven. First character of every word capitalized, everything else is lowercase.
print("i can't believe it's already mid-july.".title()) # I Can't Believe It'S Already Mid-July. 




# Using 'capwords' function to break at whitespace.
import string
print(string.capwords("i can't believe it's already mid-july.")) # I Can't Believe It's Already Mid-july.





# 'str.swapcase'
print("What's up?".swapcase())                          # wHAT'S UP? Every uppercase letter converted to lowercase, and vice versa.
print('456ABC'.swapcase())                              # 456abc
print('456ABC'.swapcase().swapcase())                   # 456ABC. First call to 'swapcase' returns original string with the case swapped; the second swaps the case on that return value. 






# Character Classification: 'str.isalpha()', 'str.isdigit()'

# 'str.isalpha()'
'Hello'.isalpha()                       # True. All characters of 'str' are alphabetic.
'Good-bye'.isalpha()                    # False. '-' is not a letter.
'Four score'.isalpha()                  # False. White space between 'Four' and 'score' is not a letter.
''.isalpha()                            # False.



# 'str.isdigit()'                       
'12340'.isdigit()                       # True. All characters are a digit.
'123.4'.isdigit()                       # False. '.' is not a digit.
'-1234'.isdigit()                       # False. '-' is not a digit.
''.isdigit()                            # False.
