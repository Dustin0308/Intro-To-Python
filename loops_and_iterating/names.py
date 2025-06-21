# Iterating over a list of names and creating a new list that contains the names in uppercase.

# Using 'while' loop

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    upper_name = names[index].upper()
    upper_names.append(upper_name)
    index += 1

print(upper_names)



# Using 'for' loop

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)





# Controlling loops: Suppose we want all the uppercase names in our 'upper_names' list except 'Max'.
# The 'continue statement can help us do that

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name == 'Max':
        continue

    upper_name = name.upper()
    upper_names.append(upper_name)

print(upper_names)                  # The result doesn't contain 'Max'.







# Rewriting a loop that uses 'continue' with a negated 'if' conditional:

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

for name in names:
    if name != 'Max':
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names)                  # The result doesn't contain 'Max'.
