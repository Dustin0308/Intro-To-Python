# Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)                   # True
print('Butter' in cats)                         # False. Butter is not the same as Butterscotch. The strings must match exactly.
print('Butter' in cats[3])                      # True. Butter does appear in Butterscoth at index 3.
print('cheddar' in cats)                        # False
