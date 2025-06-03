# Write a function called 'find_largest' that takes three number arguments and returns the largest
# of the three. Use the 'max' built-in function that you learned about in the chapter. 

# Example
# find_largest(10, 5, 20)     # should return 20

# find_largest(-10, -5, -1)   # should return -1

# num1 = 2
# num2 = 4
# num3 = 7

def find_largest(num1, num2, num3):
    result = max(num1, num2, num3)
    return float(result)

