# Create a function called 'get_min_max' that takes a list of numbers and returns both the minimum
# and maximum values as a tuple.

def get_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return (minimum, maximum)

list_1 = [1, 3, 2, 6, 7, 8]
result = get_min_max(list_1)
print(result)

# Result is (1, 8)
