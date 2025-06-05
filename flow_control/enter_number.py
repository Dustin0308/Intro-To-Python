# Write a Python program that asks the user to enter a number between 1 and 10. The program should 
# tell the user if the number is less than 5, equal to 5, or greater than 5.



def enter_number(number):
    if number < 5:
        print(f'{number} is less than 5.')
    elif number == 5:
        print(f'{number} is equal to 5.')
    else:
        print(f'{number} is greater than 5.')

user_input = input('Enter a number between 1 and 10: ')
user_number = float(user_input)
enter_number(user_number)
