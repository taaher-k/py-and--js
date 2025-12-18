#5.1.3

# main.py

import circle

def main():
    radius = float(input("Enter the radius of the circle: "))
    print(f"Area of circle with radius {radius} = {circle.calculate_circle_area(radius):.2f}")
    print(f"Perimeter of circle with radius {radius} = {circle.calculate_circumference(radius):.2f}")

if __name__ == "__main__":
    main()
