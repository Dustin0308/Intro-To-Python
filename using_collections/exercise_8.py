# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# Taking a slice of the string '[21:35]' first before calling 'rfind', the method takes that slice
# and returns the index of the character in that sliced portion. In comparison, when you call 'rfind'
# first, and then state the 'start:stop', it searches the entire string. For example, on Line 5,
# 'rfind' is searching the string 'for the fjords' and returns 8, which is the rightmost instance
# of an 'f'. On Line 6, however, it searches the rightmost 'f' between indexes 21 and 35 and 
# returns the first occurence of 'f' which is 29. 
