# Arguments & Parameters

print('hello')
print('hi')
print('how do you do')
print('Quite all right')

# Instead of calling 'print' every time we want to output something, we want to have code we can
# call when we need to print something. The above code can be updated to this:

def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

# The benifit in the above code is we have extracted the logic for displaying text in a way
# that makes our program more flexible. If we need to change the output style, we can change
# it in one place: the 'say' function - no other code has to be changed. 

# The names between the parentheses in the functon definition are called 'parameters' 
# (the above code is 'text'). They are basically placeholders for potential arguments, 
# while arguments are the values assigned to those placeholders (the above code would be 
# 'hello, hi, how do you do, and Quite all right' assigned to 'text'). So, the argument 'hello' is
# assigned to the 'text' parameter, as an example. 

# Functions give the ability to make changes in one location as shown below:

def say(text):
    print('==> ' + text)

say('hello')
say('hi')
say('how are you')
say("I'm fine")

# We have added '==>' by changing one line of code. The '==>' would appear before the argument
# assigned to the parameter 'text' every time this function is invoked.
