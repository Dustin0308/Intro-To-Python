# Using 'zip' with iterables

iterable1 = [1, 2, 3]
iterable2 = ('Kim', 'Leslie', 'Bertie')
iterable3 = [None, True, False]

zipped_iterables = zip(iterable1, iterable2, iterable3)
print(list(zipped_iterables))         # [(1, 'Kim', None), (2, 'Leslie', True), (3, 'Bertie', False)]


# zip's collection arguments are usually the same length but don't have to be. If you want to 
# enforce identical lengths, add a 'strict=True' keyword argument to the invocation

zipped_iterables = zip(iterable1, iterable2, iterable3, strict=True)


# If the lengths differ and 'strict=True' is not given, 'zip' stops after exhausting the shortest
# iterable.

result = zip(range(5, 10),          # length is 5
             range(1, 3),           # length is 2 (shortest)
             range(3, 7))           # length is 4
print(list(result))                 # [(5, 1, 3), (6, 2, 4)]
