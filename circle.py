"""
Author: ybwrdwg

abstract: asks the user for the diameter of a circle, then asks if the user wants to know the area OR the circumference, then returns the correct answer.

"""
import math

# Ask user for circle diameter and stores it's radius as an integer radie_int

radie_str = input("Hi let's try and calculate the circumference of a circle OR the area.\nWhat is the diameter of said circle? \n")

radie_float = float(radie_str)
radie_float = (radie_float)/2

choose_area_or_circumference =(input("Do you wish to know the area or the circumference?\n"))

#calculates the circumference and area of our circle and stores them as circle_circumference and circle_area

circle_area = (math.pi)*((radie_float)**2)
circle_circumference = (math.pi)*(radie_float)*2

choice = choose_area_or_circumference.lower()

if "area" in choice:
    print("The area of such circle is ")
    print(circle_area)
else:
    if "circumference" in choice:
        print("The circumference of such circle is ")
        print(circle_circumference)
    else:
        print ("error")
