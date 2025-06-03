# Which of the identifiers in the following program are function names? Which are method names?
# Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))


# Function Names:
# say: not built-in
# print: built-in
# input: built-in
# max: built-in

# Method Names:
# upper
# lower
