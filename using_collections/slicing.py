string = 'abcdefghi'
print(string[3:7])                          # defg
print(string[-6:-2])                        # defg
print(string[2:8:2])                        # ceg
print(repr(string[3:3]))                    # ''. Empty slice when start/stop values are the same.
print(string[:])                            # abcdefghi. Duplicate of string (shallow copy).
print(string[::-1])                         # ihgfedcba. Reversed copy of string.

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[3:7])                             # [4, 5, 6, 7]
print(seq[-6:-2])                           # [5, 6, 7, 8]
print(seq[2:8:2])                           # [3, 5, 7]
print(seq[3:3])                             # []
print(seq[:])                               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(seq[::-1])                            # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

seq = [[1, 2], [3, 4]]
seq_dup = seq[:]
print(seq[0] is seq_dup[0])                 # True. Demonstrates that slicing performs a shallow
                                            # copy if the sequence contains any collections.
