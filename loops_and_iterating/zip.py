# Suppose you want to print the full names of several thousand people. You have two lists: one 
# contains the forenames, and the other contains the corresponding surnames. Without 'zip', you
# need to use a 'while' loop and indexing.

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

index = 0
while index < len(forenames):
    if index >= len(surnames):              # surnames might be shorter
        break

    forename = forenames[index]
    surname = surnames[index]
    print(f'{forename} {surname}')

    index += 1




# Here's how to do the same thing using zip, for less work, easier code. 

forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

zipped_names = zip(forenames, surnames)     # 'zip' creates a lazy sequence that acts like a list of tuples, that contain a forename and surname.
for forename, surname in zipped_names:      # This is where the loop starts.
    print(f'{forename} {surname}')
