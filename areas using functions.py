import math

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_circle(radius):
    return math.pi * radius * radius

def area_of_square(side):
    return side * side

def area_of_rectangle(length, width):
    return length * width

def main():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    print(f"Area of Triangle: {area_of_triangle(base, height)}")
    
    radius = float(input("Enter the radius of the circle: "))
    print(f"Area of Circle: {area_of_circle(radius)}")
    
    side = float(input("Enter the side of the square: "))
    print(f"Area of Square: {area_of_square(side)}")
    

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    print(f"Area of Rectangle: {area_of_rectangle(length, width)}")

if __name__ == "__main__":
    main()

