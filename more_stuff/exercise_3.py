# Consider the following code:

# def sum_of_squares(num1, num2):
#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)

# Write a nested function in sum_of_squares that will make this code work as shown.


def sum_of_squares(num1, num2):
    def square(number):              # Added nested function to calculate the square of the number
        return number * number       # passed to it as an argument.
    
    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)
