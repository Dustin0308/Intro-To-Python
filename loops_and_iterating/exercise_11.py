# Challenging Problem: Don't feel bad if you struggle with this problem or can't solve it. The 
# problem is not easy. It is designed to demonstrate why we prefer to use 'for' loops when we can, 
# and a big part of that problem is messy code that is difficult to write and understand. See how far 
# you can get, but don't spend much time struggling.


# Print all of the even numbers in the following list of nested lists. This time, don't use any 'for' 
# loops.

# Expected Output:
# 6
# 4
# 2
# 4
# 16
# 0

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        number = my_list[outer_index][inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1
    
    outer_index += 1

# Or by assigning each nested list to a local variable which simplifies the code:

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0
while outer_index < len(my_list):
    inner_list = my_list[outer_index]
    inner_index = 0
    while inner_index < len(inner_list):
        number = inner_list[inner_index]
        if number % 2 == 0:
            print(number)

        inner_index += 1

    outer_index += 1
