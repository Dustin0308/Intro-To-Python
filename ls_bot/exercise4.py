# Write a program that converts temperature from Fahrenheit to Celsius. The formula is:
# C = (F-32) * 5/9. 
# Use variables to store the temperatures. 


f = input('Enter current temperature in Fahrenheit:')
c = (int(f) - 32) * (5 / 9)
print(f'{f} in fahrenheit is {c} in Celsuis.')
