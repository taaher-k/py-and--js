class MarksCollector:
    def __init__(self):
        self.__marks = []   # private attribute
        self.__count = 1
        self.__subjects = 0

    def get_subjects(self):
        while True:
            try:
                subject = int(input("Enter number of subjects: "))
                if subject <= 0 or subject > 100:
                    print("Number of subjects must be between 1 and 100. Try again.")
                    continue
                self.__subjects = subject
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for number of subjects.")

    def collect_marks(self):
        for _ in range(self.__subjects):
            while True:
                try:
                    marks = int(input(f"Enter your marks for subject {self.__count}: "))
                    if marks < 0 or marks > 100:
                        print("Marks should be between 0 and 100. Try again.")
                        continue
                    self.__marks.append(marks)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer for marks.")
            self.__count += 1

    def display_marks(self):
        print(f"Your marks are: {self.__marks}")

    def find_average(self):
        if self.__marks:
            return sum(self.__marks) / len(self.__marks)
        return 0

    # Protected getter for marks (so child class can use them)
    def _get_marks(self):
        return self.__marks


# Child class inherits from MarksCollector
class StudentMarksCollector(MarksCollector):
    def __init__(self, student_name):
        super().__init__()   # call parent constructor
        self.student_name = student_name

    def display_student_info(self):
        print(f"Student Name: {self.student_name}")
        self.display_marks()
        print(f"Average Marks: {self.find_average()}")

    def highest_mark(self):
        marks = self._get_marks()
        return max(marks) if marks else None

    def lowest_mark(self):
        marks = self._get_marks()
        return min(marks) if marks else None

student = StudentMarksCollector("Taaher")
student.get_subjects()
student.collect_marks()
student.display_student_info()

print(f"Highest Mark: {student.highest_mark()}")
print(f"Lowest Mark: {student.lowest_mark()}")
