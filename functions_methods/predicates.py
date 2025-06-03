# Functions that always return a Boolean value are called predicates:

def is_digit(char):
    if char >= '0' and char <= '9':
        return True
    
    return False
