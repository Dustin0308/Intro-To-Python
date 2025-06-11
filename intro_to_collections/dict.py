# Dicts have the following characteristics: 
 
# Dicts are mutable.

# The keys in a dict must be unique. Trying to add a duplicate key to a dict merely replaces the 
# existing key's associated value.

# Keys must be "hashable" values. We won't define "hashable" right now. However, hashable values are 
# usually (not always) immutable. All built-in immutable types (numbers, strings, booleans, tuples, 
# frozen sets, and None) are hashable and can be dict keys.

# The values in each key/value pair may be any object.

d = {'a': 1, (1, 3): 3, 1: 'x'}
print(d)         # {'a': 1, (1, 3): 3, 1: 'x'}
print(d['a'])    # 1
print(d[(1, 3)]) # 3
print(d[1])      # 'x'

d['a'] = 'A'
print(d)        # {'a': 'A', (1, 3): 3, 1: 'x'}
