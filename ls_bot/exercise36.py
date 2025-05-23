# What is the purpose of the 'end' parameter in the 'print()' function? Provide an example of
# when you might use it.

# The puropose of the 'end' character is to define what 'print()' prints after the last argument. 
# Normally, it prints a newline. You might use this for compatibilty with Windows or for
# suppressing the newline altogether. 

print(1, 2, 3, end=' <-\n')
