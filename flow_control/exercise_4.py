# Refactor this code to use a regular 'if' statement instead.

def baz():
    return ('bar' if foo() else qux())

# The above code is an EXCELLENT example of using the ternary expression; the refactoring
# demonstrates how the tenary works.

def baz():
    if foo():
        return 'bar'
    else:
        return qux()
    