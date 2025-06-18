# Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]              # True
numbers2 = []                               # False
numbers3 = [2, 4, 6, 8]                     # False
numbers4 = ['1', '3', '5']                  # False. 3 is not the same as '3'. '3' is a string, 3 is an integer.
numbers5 = ['1', 3.0, '5']                  # True. 3 == 3.0. *REMEMBER*: 'in' checks for VALUE EQUALITY.

# You should print 'True' or 'False' depending on each result.

print(3 in numbers1)                        # True
print(3 in numbers2)                        # False
print(3 in numbers3)                        # False
print(3 in numbers4)                        # False
print(3 in numbers5)                        # True

# Or it can be written like this:

print(3 in numbers1, 3 in numbers2, 3 in numbers3, 3 in numbers4, 3 in numbers5)
