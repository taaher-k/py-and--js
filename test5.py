import os
import shutil

def menu():
    while True:
        print("\n=== File & Directory Operations Menu ===")
        print("1. Create Directory")
        print("2. List Directory Contents")
        print("3. Rename File")
        print("4. Delete File")
        print("5. Delete Directory")
        print("6. Copy File")
        print("7. Move File")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            dirname = input("Enter directory name to create: ")
            try:
                os.mkdir(dirname)
                print(f"Directory '{dirname}' created successfully.")
            except FileExistsError:
                print(f"Directory '{dirname}' already exists.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            path = input("Enter directory path (leave blank for current): ")
            if path.strip() == "":
                path = "."
            try:
                contents = os.listdir(path)
                print(f"Contents of '{path}':")
                for item in contents:
                    print(item)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            old_name = input("Enter current file/directory name: ")
            new_name = input("Enter new name: ")
            try:
                os.rename(old_name, new_name)
                print(f"Renamed '{old_name}' to '{new_name}'.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            filename = input("Enter file name to delete: ")
            try:
                os.remove(filename)
                print(f"File '{filename}' deleted successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            dirname = input("Enter directory name to delete: ")
            try:
                os.rmdir(dirname)  # only works if directory is empty
                print(f"Directory '{dirname}' deleted successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            src = input("Enter source file path: ")
            dest = input("Enter destination file path: ")
            try:
                shutil.copy(src, dest)
                print(f"File '{src}' copied to '{dest}'.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "7":
            src = input("Enter source file path: ")
            dest = input("Enter destination file path: ")
            try:
                shutil.move(src, dest)
                print(f"File '{src}' moved to '{dest}'.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "8":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


# Run the menu
menu()



import csv

def dict_to_tuples_and_csv():
    # Example dictionary
    my_dict = {
        "name": "Taaher",
        "age": 24,
        "dept": "Computer Applications",
        "gpa": 3.95
    }

    # Convert dictionary items to list of tuples
    tuple_list = list(my_dict.items())

    # Display results
    print("Original Dictionary:", my_dict)
    print("List of Tuples:", tuple_list)

    # Write tuples into a CSV file
    with open("dict_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Key", "Value"])  # header row
        writer.writerows(tuple_list)

    print("\nData has been written to 'dict_data.csv' successfully.")


# Run the function
dict_to_tuples_and_csv()
