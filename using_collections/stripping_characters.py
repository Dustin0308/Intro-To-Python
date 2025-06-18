# Using the 'str.strip' method to return a copy of 'str' with all leading and trailing whitespace
# characters removed.

text = ' \t abc def \n\r'
print(repr(text))                       # ' \t abc def \n\r'
print(repr(text.strip()))               # 'abc def'
