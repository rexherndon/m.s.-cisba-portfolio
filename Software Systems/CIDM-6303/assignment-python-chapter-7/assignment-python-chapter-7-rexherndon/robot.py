# Create a Robot class according to the instructions
# import random will have functions useful for this assignment
import random

# Start coding here...





















# Test code. DO NOT CHANGE THIS TEST CODE
try: 
    r = Robot("Marvin")
    r.hello()
    r.sing()
    r.count(10)
    r.how_do_you_feel()
except AttributeError as err:
    print("***Test failed***")
    print("Missing a method. Making progress but not done yet. Keep coding and try again.")
    print(err)
else: 
    print("Test successful. Your code passes")