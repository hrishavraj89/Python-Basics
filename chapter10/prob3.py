# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Prob3:
    a = 5

object = Prob3()
print(object.a)
object.a = 0
print(object.a)

print(Prob3.a)  #Class attribute value unchanged!

# This means that changingg the value of 'a' using 'object.a' does not change the value of the class attribute.
#     It rather creates another value of a which is given preference