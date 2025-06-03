# Sometimes, a method mutates the object used to invoke the method: it 'mutates the caller'.
# In the following code, the 'pop' method mutates the caller (the list referenced by 'odd_numbers'.)

odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop()
print(odd_numbers)

# The 'pop' method without arguments removes and returns the last element, which is '9' in the 
# above example. 
