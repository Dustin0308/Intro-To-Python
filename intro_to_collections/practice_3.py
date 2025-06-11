# Create a function that takes a string and returns a dictionary where the keys are the characters 
# in the string and the values are the number of times each character appears.

def char_count(string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] = count_dict[char] + 1
        else:
            count_dict[char] = 1
    return count_dict

print(char_count('hello'))
print(char_count('goodbye'))
print(char_count('how are you'))
