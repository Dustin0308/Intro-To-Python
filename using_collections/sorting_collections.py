# Sortin collections using the 'sorted' function.

names = ('Grace', 'Clare', 'Allison', 'Trevor')     # Tuple of names.
print(sorted(names))                                # ['Allison', 'Clare', 'Grace', 'Trevor']. Sorted to a list. 

print(names)                                        # ('Grace', 'Clare', 'Allison', 'Trevor'). Original tuple is unchanged.

names = list(names)                                 # Converted tuple to list.
print(names)                                        # ['Grace', 'Clare', 'Allison', 'Trevor']

print(names.sort())                                 # None. Collection was mutated.
print(names)                                        # ['Allison', 'Clare', 'Grace', 'Trevor']




# Reverse sorting by using 'reverse=True' to the argument list. 

names = ['Grace', 'Clare', 'Allison', 'Trevor']
print(sorted(names, reverse=True))                  # ['Trevor', 'Grace', 'Clare', 'Allison']. Sorted in reverse. See line 11 above for reference.



names.sort(reverse=True)
print(names)                                        # ['Trevor', 'Grace', 'Clare', 'Allison']. Sorted in reverse. See line 11 above for reference.



# Using 'key=func' to sort, specificially 'key=str.casefold' to perform a case-insensitive sort.

words = ['abc', 'DEF', 'xyz', '123']
print(sorted(words))                                # ['123', 'DEF', 'abc', 'xyz']. Sorted least to greatest. 



print(sorted(words, key=str.casefold))              # ['123', 'abc', 'DEF', 'xyz']. Sorted case-insensitive.





# Sorting a list of numeric-valued strings by passing 'key=int' to the function or method.

numbers = ['1', '5', '100', '15', '534', '53']
numbers.sort()
print(numbers)                                      # ['1', '100', '15', '5', '53', '534']


numbers.sort(key=int)
print(numbers)                                      # ['1', '5', '15', '53', '100', '534']
