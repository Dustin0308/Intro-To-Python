print(min(-10, 5, 12, 0, -20))
print(max(-10, 5, 12, 0, -20))

print(min('over', 'the', 'moon'))
print(max('over', 'the', 'moon'))

print(max(-10, '5', '12', '0', -20))  # Should give a TypeError: '>' not supported between
                                      # instances of 'str' and 'int'.

# Using 'max' and 'min' with a single iterable argument, such as a list, set, or tuple.

my_tuple = ('i', 'tawt', 'i', 'taw', 'a',
            'puddy', 'tat')
print(min(my_tuple))
print(max(my_tuple))
