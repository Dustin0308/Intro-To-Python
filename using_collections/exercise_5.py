# Which of the following values can't be used as a key in a dict object, and why?

'cat'                                       # Can be used. Immutable. Acceptable as dict keys.
(3, 1, 4, 1, 5, 9, 2)                       # Can be used. Immutable. Acceptable as dict keys.
['a', 'b']                                  # Can't be used. This is a list which is mutable.
{'a': 1, 'b': 2}                            # Can't be used. Mutable. 
range(5)                                    # Can be used. Immutable.
{1, 4, 9, 16, 25}                           # Can't be used. Mutable.
3                                           # Can be used. Immutable.
0.0                                         # Can be used. Immutable.
frozenset({1, 4, 9, 16, 25})                # Can be used. Immutable.


# Can't be used:
['a', 'b']
{'a': 1, 'b': 2}
{1, 4, 9, 16, 25}
