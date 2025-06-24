# In your own words, explain the difference between these two expressions.

my_object1 == my_object2                # This tests value equality
my_object1 is my_object2                # This tests object equality

# Line 3 means 'my_object1' has the same value as 'my_object2' if it returs 'True' and doesn't if
# it returns 'False'. '==' tests value equality.

# Line 4 means 'my_object1' is the same object as 'my_object2' if it returns 'True' and isn't if it
# returns 'False'. 'is' tests object equality.


# Launch School's solution:

# my_object1 == my_object2 compares two objects to see whether they are equal. They are considered 
# equal when they have the same value or state. In the case of collections, two collections are 
# equal when they have the same elements.

# my_object1 is my_object2 checks two variables to see whether they reference the same object. An 
# object is the same as another object if both are stored at the same location in memory. In 
# particular, that means we can say that my_object1 and my_object2 share the referenced object or 
# that my_object1 and my_object2 are aliases for the same object.
