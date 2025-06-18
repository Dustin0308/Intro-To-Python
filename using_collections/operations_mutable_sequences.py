# Adding Elements to Mutable Sequences using 'append', 'insert', and 'extend' methods

# 'seq.append'

numbers = [1, 2]

numbers.append(10)                      # Append the number 10
print(numbers)                          # [1, 2, 10]


# 'seq.instert'

numbers = [1,2]

numbers.insert(0, 8)                    # Insert 8 before numbers [0]
print(numbers)                          # [8, 1, 2]
numbers.insert(2, 6)                    # Insert 6 before nubmers[2]
print(numbers)                          # [8, 1, 6, 2]

# 'seq.extend'

numbers = [1, 2]

numbers.extend([7, 8])                  # Append 7 and 8 to numbers
print(numbers)                          # [1, 2, 7, 8]
