# Using 'index' and 'count' in sequences

names = ['Karl', 'Grace', 'Clare', 'Victor', 'Antonina', 'Allison', 'Trevor']

print(names.index('Clare'))                 # 2
print(names.index('Trevor'))                # 6
print(names.index('Chris'))                 # ValueError: 'Chris' is not in list

numbers = [1, 3, 6, 5, 4, 10, 1, 5, 4, 4, 5, 4]

print(numbers.count(1))                     # 2. '1' appears 2 times in the sequence.
print(numbers.count(3))                     # 1. '3' appears 1 time in the sequence.
print(numbers.count(4))                     # 4. '4' appears 4 times in the sequence.
print(numbers.count(7))                     # 0. '7' appears 0 times in the sequence.

# Indexing with strings

names = 'Karl Grace Clare Victor Antonina Trevor'

print(names.index('Clare'))                 # 11. Appears at the 11th index.
print(names.index('Trevor'))                # 33. Appears at the 33rd index.
print(names.index('Chris'))                 # ValueError: substring not found. 
