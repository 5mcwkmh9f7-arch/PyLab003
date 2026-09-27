# Calculates the area of a rectangle using a custom function


def calculate_area(length, width):
    """Return the area of a rectangle given its length and width."""
    return length * width


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = calculate_area(length, width)

print(f"The area of a rectangle with length {length} and width {width} is {area:.2f}")