import sys

def multiply_numbers():
    # Check if numbers are provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <num1> <num2> <num3> ...")
        return

    try:
        # Convert arguments to integers/floats
        numbers = [float(arg) for arg in sys.argv[1:]]

        # Multiply all numbers
        result = 1
        for num in numbers:
            result *= num

        # Display result
        print("Numbers:", numbers)
        print("Product:", result)

    except ValueError:
        print("Error: Please provide valid numbers.")


# Run the function
if __name__ == "__main__":
    multiply_numbers()
