# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins 
# with the first c.

my_str = 'Launch School'
print(my_str[4:10])                     # ch Sch


# You can also do it this way as per Launch School

start = my_str.find('c')
print(my_str[start:start + 6])          # ch Sch
