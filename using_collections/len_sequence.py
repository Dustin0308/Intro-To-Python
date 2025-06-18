# Using 'len' to determine a sequence's length

seq = ('a', 'b', 'c')
if len(seq) > 3:
    print(seq[3])


# To access the last element in a sequence

seq = ('a', 'b', 'c')
last_index = len(seq) - 1
print(seq[last_index])              # c


# Using negative indexes

seq = ('a', 'b', 'c')
print(seq[-1])                      # c (last element)
print(seq[-2])                      # b (next to last element)
print(seq[-3])                      # a (2nd to last element)



# To change the value of an element in a mutable sequence

seq = ['a', 'b', 'c']
seq[1] = 'B'
print(seq)                          # ['a', 'B', 'c']
