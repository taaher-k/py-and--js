import sys

def reverse_file_content():
    # Check if filename is provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        return

    filename = sys.argv[1]

    try:
        # Open file and read content
        with open(filename, "r") as f:
            content = f.read()

        # Reverse content
        reversed_content = content[::-1]

        # Display output
        print("=== Original Content ===")
        print(content)
        print("\n=== Reversed Content ===")
        print(reversed_content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

import os
import subprocess

def create_directory():
    dirname = "pythonPrograms"

    try:
        # Check if directory already exists
        if os.path.exists(dirname):
            print(f"Directory '{dirname}' already exists.")
        else:
            # Run the mkdir shell command
            subprocess.run(["mkdir", dirname], check=True)
            print(f"Directory '{dirname}' created successfully.")

    except subprocess.CalledProcessError:
        print("Error: Could not create directory.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the function
create_directory()



# Run the function
if __name__ == "__main__":
    reverse_file_content()


