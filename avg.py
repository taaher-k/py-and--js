def collect_marks():
    y = []
    count = 1

    try:
        subject = int(input("Enter number of subjects: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer for number of subjects.")
        return []   # return empty list if input fails

    for x in range(subject):
        while True:  # keep asking until valid marks are entered
            try:
                marks = int(input(f"Enter your marks for subject {count}: "))
                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100. Try again.")
                    continue
                y.append(marks)
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for marks.")
        count += 1

    print(f"Your marks are: {y}")
    return y   # return the list so you can use it later


# Example usage
marks_list = collect_marks()

if marks_list:  # only calculate average if list is not empty
    def find_average_list(numbers):
        return sum(numbers) / len(numbers)

    print(f"Your average marks are: {find_average_list(marks_list)}")
