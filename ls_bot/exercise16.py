# What is the difference between reassignment and mutation? Give an example of each. 

# Answer

# The difference between reassignment and mutation is reassignment points a object to a 
# completely new value, while mutation changes the existing value of an object internally. 

# Examples of each

count = 10          # Initialization
count = 15          # Reassignment
print(count)        # outputs 15

my_list = [1, 2, 3] # Initialization
my_list[0] = 5      # Mutation
print(my_list)      # outputs [5, 2, 3]
