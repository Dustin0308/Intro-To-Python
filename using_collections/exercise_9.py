# Write some code to replace the value 6 in the following nested list with 606:

stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)

# print(stuff[1][3])    # 6. Found the instance of '6' at indexes '[1][3]'. Then applied the change
# to that index on Line 9. Then called to print to show the change: 
# [['hello', 'world'], ['example', 'mem', None, 606, 88], [4, 8, 12]].
