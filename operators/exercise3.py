# Exercise 3

# Obtain the radius and lenght of a circle.

# area = pi*radius**2
# perimeter_lenght = 2*pi*radius

# Present the results with only two decimals

import math

radius = float(input("Please, enter the radius of the circle: "))
area = math.pi*radius**2
perimeter_lenght = 2*math.pi*radius

print(f"The area of the circle is {area:.2f}")
print(f"The lenght of the perimeter of the circle is {perimeter_lenght:.2f}")