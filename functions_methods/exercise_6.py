# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return                          # This ends the function invocation. There is no value after it.
    print(words)

scream('Yipeee')

# Nothing. No output. The 'return' on line 5 terminates the function before it can print anything.
