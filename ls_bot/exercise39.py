# Write a program that converts temperature from Celsius to Fahrenheit. The formula is:
# F = (C x 9/5) + 32

celsius = float(input('What is the temperaute at your current location? '))
fahrenheit = (celsius * (9 / 5)) + 32
print(f'Your current temperature of {celsius} celsius is {fahrenheit} in fahrenheit!')
