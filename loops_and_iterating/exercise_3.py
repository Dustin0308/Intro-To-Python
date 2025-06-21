# Use a 'while' loop to print the numbers in 'my_list', one number per line. Then, do the same with 
# a 'for' loop.

# Expected output:
# 6
# 3
# 0
# 11
# 20
# 4
# 17

my_list = [6, 3, 0, 11, 20, 4, 17]







# 'while' loop

my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    number = my_list[index]
    print(number)
    index += 1





# 'for' loop

my_list = [6, 3, 0, 11, 20, 4, 17]

for number in my_list:
    print(number)
