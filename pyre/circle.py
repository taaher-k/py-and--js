#5.1.3
import math 


def calculate_circle_area(radius):   
     """Calculate the area of a circle given its radius."""
     if radius < 0:
         raise ValueError("Radius cannot be negative.")

     area_of_circle = math.pi * radius * radius
     return area_of_circle


def calculate_circumference(radius):
    """Calculate the circumference of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")

    circumference = 2 * math.pi * radius
    return circumference

# Example usage
if __name__ == "__main__":
    try:
        r = float(input("Enter the radius: "))
        print(f"Area of circle with radius {r} = {calculate_circle_area(r):.2f}")
    except ValueError as e:
        print("Error:", e)

    try:
        r =float(input("Enter the radius: "))
        print(f"Circumference of circle with radius {r} = {calculate_circumference(r):.2f}")
    except ValueError as e:
        print("Error:",e)    

