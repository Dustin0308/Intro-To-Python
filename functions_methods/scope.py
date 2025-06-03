# The scope of an identifier determines where you can use it. Python determines scope by looking 
# at where you initialize the identifier. In Python, identifiers have function scope. That means 
# that anything initialized inside a function is only available within the body of that function 
# and any nested functions. No code outside of the function body can access that identifier.

# def well_howdy(who):
#    greeting = 'Howdy'
#    print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

# This code will give an error message: NameError: name 'greeting' is not defined. This error 
# occurs since the 'greeting' variable is only available inside the 'well_howdy' function.
# The surrounding code has no way to access the variable.

# What happens if we define our gretting variable in the outer scope? (Comment out the above code)

# greeting = 'Salutations'

# def well_howdy(who):
#    greeting = 'Howdy'
#    print(f'{greeting}, {who}')

# well_howdy('Angie')
# print(greeting)

# Will output: 'Howdy, Angie' and then on the next line, 'Salutations'. Greeting is on scope on
# line 26, but the 'greeting' variable on line 22 plays no part in the function's body as 
# the assignment on line 22 hides the 'greeting' variable from line 19. This is called 
# 'variable shadowing'.

# If we remove the assignment on line 22: 

greeting = 'Salutations'

def well_howdy(who):
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)

# Without any assigments in the function body, Python looks for 'greeting' in the lexical scope,
# which means it searches the outer scope for the nearest definition of 'greeting'.
