# Write a program that asks the user to enter a single letter. The program should then determine if 
# the letter is a vowel (a, e, i, o, u) or a consonant, and print an appropriate message. Make sure 
# your program handles both uppercase and lowercase letters correctly.



def single_letter(letter):
    vowel = 'aeiou'
    if letter.lower() in vowel:
        print('Your letter is a vowel.')
    else:
        print('Your letter is a consonant.')

user_input = input('Please enter a letter: ')
single_letter(user_input)
