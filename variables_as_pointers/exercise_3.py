# Without running this code, what will it print? Why?

dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])


# Line 9 above sets a new dict to 'dict2' which creates a new dict object.
# Line 10, changed the key 'Monty Python' to 'Holy Grail' with the value of 'The Life of Brian'.
# Line 11, prints the value of 'dict1' key 'Monty Python' (left unchanged due to the new dict). 
# # 'dict1' and 'dict2' are not the same objects due to the change on line 9. So, it should print:

# 'The Life of Brian' which is the value for the key 'Monty Python' in dict 1.
