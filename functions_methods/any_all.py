# Both the 'any' and 'all' functions operate on iterable collections, such as lists, tuples
# ranges, dictionaries, and sets.

# The 'any' function returns 'True' if any elements in a collection is truhy, 'False' if all
# of the elements are falsy. The 'all' function returns 'True' if all of the elements are 
# truthy, 'False' otherwise. 

collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1))             # Should return False
print(any(collection2))             # Should return True
print(any(collection3))             # Should return True        
print(any([]))                      # Should return False. None of the elements are truthy.

print(all(collection1))             # Should return False
print(all(collection2))             # Should return False
print(all(collection3))             # Should return True
print(all([]))                      # Should return True. None of the elements are falsy.
