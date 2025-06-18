# Using 'min' and 'max' in iterble collections

my_set1 = {1, 4, -9, 16, 25, -36, -63, -1}
my_set2 = {'1', '4', '-9', '16', '25', '-36', '-63', '-1'}

print(min(my_set1), max(my_set1))                   # -63 25
print(min(my_set2), max(my_set2))                   # -1 4


# Using 'min' and 'max' with multiple arguments instead of an iterable. 

print(min(3, 5, -1), max(3, 5, -1))                 # -1 5
