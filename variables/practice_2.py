# Augmented assignment with strings

bar = 'xyz'             # bar is 'xyz'
bar += 'abc'            # bar is now 'xyzabc'
bar *= 2                # bar is now 'xyzabcxyzabc'
print(bar)              # prints xyzabcxyzabc

# Augmented assignment with lists

bar = [1, 2, 3]         # bar is [1, 2, 3]
bar += [4, 5]           # + with lists appends
                        # bar is now [1, 2, 3, 4, 5]
print(bar)

# Augmented assignment with sets

bar = {1, 2, 3}         # bar is {1, 2, 3}
bar |= {2, 3, 4, 5}     # | performs set union
                        # bar is now {1, 2, 3, 4, 5}
bar -= {2, 4}           # - performs set difference
                        # bar is now {1, 3, 5}
print(bar)
