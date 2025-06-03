# What does the following code print?

def scream(words):
    return words + '!!!!'

scream('Yipeee')

# It doesn't output anything. The function returns a value 'Yipeee!!!!' but doesn't do anything with
# it including printing it. If we want to see it print the correct value, we would rewrite the 
# code like this: 

def scream(words):
    return words + '!!!!'

print(scream('Yipeee'))
