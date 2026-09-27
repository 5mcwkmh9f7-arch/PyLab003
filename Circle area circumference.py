# Calculates the area and circumference of a circle using the math module

import math

radius = int(input("Enter the radius of the circle (whole number): "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")