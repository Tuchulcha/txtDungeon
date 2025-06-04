"""
Author: ybwrdwg <kasta.sten@gmail.com>
Filestatus: incomplete
The class Die 
"""
import random


class Die:
    def __init__(self, number_of_sides, facevalue=1): # default facevalue
        self.number_of_sides = number_of_sides
        self.facevalue = facevalue # Initial face value (e.g., 1 when created)
    def roll(self): 
        """Rolls the die and sets the facevalue to a random number."""
        self.facevalue = random.randint(1, self.number_of_sides)
        return self.facevalue

    def get_facevalue(self):
        """Returns the current face value of the die."""
        return self.facevalue

    def __str__(self): # Added a string representation for easy printing
        return f"A {self.number_of_sides}-sided die showing {self.facevalue}"

# --- How to use the Die class ---

# Create a 6-sided die
my_die = Die(6)
print(my_die) # Output: A 6-sided die showing 1 (or whatever default you set)
class Die:
    def __init__(self, number_of_sides, facevalue):
        #self.number_of_sides = numbers_of_sides
        self.facevalue = facevalue
        self.random_value = 1
    #def die-print(input("number")):
        #y = int(input)
        #print(y):


# Roll the die
print(f"Rolling the die... it landed on: {my_die.roll()}")
print(my_die) # Output will reflect the new facevalue

# Create a 20-sided die
d20 = Die(20)
print(f"Rolling a D20... it landed on: {d20.roll()}")
print(d20.get_facevalue()) 
