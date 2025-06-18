# What will the following code print?

print('abc-def'.isalpha())              # False. '-' is not a letter. 
print('abc_def'.isalpha())              # False. '_' is not a letter.
print('abc def'.isalpha())              # False. Space is not a letter.
print('abc def'.isalpha() and
      'abc def'.isspace())              # False. Spaces are not letters and letters are not spaces. 
print('abc def'.isalpha() or             
      'abc def'.isspace())              # False. Spaces are not letters and letters are not spaces.
print('abcdef'.isalpha())               # True. Every character is a letter.
print('31415'.isdigit())                # True. Every character is a digit.
print('-31415'.isdigit())               # False. '-' is not a digit.
print('31_415'.isdigit())               # False. '_' is not a digit.
print('3.1415'.isdigit())               # False. '.' is not a digit.
print(''.isspace())                     # False. String is empty.
