# Without running the following code, determine what each line should print.

print('johnson' in 'Joe Johnson')               # False. 'j' is not the same as 'J'.
print('sen' not in 'Joe Johnson')               # True.
print('Joe J' in 'Joe Johnson')                 # True.                
print(5 in range(5))                            # False. Range ends at 4.
print(5 in range(6))                            # True. Range ends at 5.
print(5 not in range(5, 10))                    # False.
print(0 in range(10, 0, -1))                    # False. Range ends at 1.
print(4 in {6, 5, 4, 3, 2, 1})                  # True.
print({1, 2, 3} in {1, 2, 3})                   # False. It would have to be a nested set to be True.
print({3, 2} in {1, frozenset({2, 3})})         # True. {3, 2} and {2, 3} are considered equal sets. For reference, if you were to use 'is' instead of 'in', it would return False. They are equal in value only. 
