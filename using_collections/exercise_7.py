# Write Python code to replace all the ':' characters in the string below with '+'.
# Try this problem using the methods you've learned about in this chapter. Once you have that working, 
# use the Python documentation for the 'str' type to find an alternative solution.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
print(info.count(':'))
print(info.replace(':', '+', 6))

# The above answer was my answer which does satisfy the solution, but the answers below were the
# solutions launch school gave. My answer using the 'replace()' method was not covered in the lesson.
# It's best to leave out the '6' in my answer to satisfy ALL occurences of the ':' character. I 
# should have also set a variable when doing so like on Line 22 below. 

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
parts = info.split(':')
result = '+'.join(parts)
print(result)

# OR

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(':', '+')
print(result)
