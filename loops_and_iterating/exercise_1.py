# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)


# There is no modification of 'counter' which would make the loop condition falsy, so it continues 
# forever. It should be written like this:

counter = 0

while counter < 5:
    print(counter)
    counter += 1
