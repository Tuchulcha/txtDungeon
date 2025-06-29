"""circle.py && = AND, || = OR, in comments.
Author: ybwrdwg

Abstract: Asks the user for the diameter of a circle.
After that ask user if user wants to know the area || the circumference
(any string that contains that phrase will suffice, capitalization neutral)
, then return correct answer
, else return "error"
"""

# Needed libraries

import math

# Ask user for circle diameter,
# Stores answer,convert to radius
# , && convert it's datatype: str -> float in: radie_float

radie_str = input(
    "Hi let's try and calculate the circumference of a circle OR the area.\nWhat is the diameter of said circle? \n"
)

radie_float = (float(radie_str)) / 2

# Ask the user if it wants to know the area || the circumference
# Make the answer lower case and match the phrases area && circumference
# Calculate the circumference & area of our circle
# Store them as floats: circle_circumference & circle_area
# Compare  the answer to a if/else statements and return correct answer
# ,else return "error"

choose_area_or_circumference = input(
    "Do you wish to know the area OR the circumference?\n"
)

circle_area = (math.pi) * ((radie_float) ** 2)

circle_circumference = (math.pi) * (radie_float) * 2

choice = choose_area_or_circumference.lower()

if "area" in choice:
    print("The area of such circle is ")
    print(circle_area)
else:
    if "circumference" in choice:
        print("The circumference of such circle is ")
        print(circle_circumference)
    else:
        print("error")


# test for ruff
