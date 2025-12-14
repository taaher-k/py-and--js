// Import readline for terminal input
const readline = require("readline");

// Create readline interface
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
}); 

// Helper function to ask questions (returns a Promise)
function askQuestion(query) {
  return new Promise(resolve => rl.question(query, ans => resolve(ans)));
}

// Parent class
class MarksCollector {
  constructor() {
    this._marks = [];   // private-like attribute
    this._count = 1;
    this._subjects = 0;
  }

  async getSubjects() {
    while (true) {
      let input = await askQuestion("Enter number of subjects: ");
      let subject = parseInt(input);

      if (!isNaN(subject)) {
        if (subject > 0 && subject <= 100) {
          this._subjects = subject;
          break;
        } else {
          console.log("Number of subjects must be between 1 and 100. Try again.");
        }
      } else {
        console.log("Invalid input! Please enter a valid integer for number of subjects.");
      }
    }
  }

  async collectMarks() {
    for (let i = 0; i < this._subjects; i++) {
      while (true) {
        let input = await askQuestion(`Enter your marks for subject ${this._count}: `);
        let marks = parseInt(input);

        if (!isNaN(marks)) {
          if (marks >= 0 && marks <= 100) {
            this._marks.push(marks);
            break;
          } else {
            console.log("Marks should be between 0 and 100. Try again.");
          }
        } else {
          console.log("Invalid input! Please enter a valid integer for marks.");
        }
      }
      this._count++;
    }
  }

  displayMarks() {
    console.log("Your marks are:", this._marks);
  }

  findAverage() {
    if (this._marks.length > 0) {
      let sum = this._marks.reduce((acc, val) => acc + val, 0);
      return sum / this._marks.length;
    }
    return 0;
  }

  _getMarks() {
    return this._marks;
  }
}

// Child class
class StudentMarksCollector extends MarksCollector {
  constructor(studentName) {
    super();
    this.studentName = studentName;
  }

  displayStudentInfo() {
    console.log(`Student Name: ${this.studentName}`);
    this.displayMarks();
    console.log(`Average Marks: ${this.findAverage()}`);
  }

  highestMark() {
    let marks = this._getMarks();
    return marks.length > 0 ? Math.max(...marks) : null;
  }

  lowestMark() {
    let marks = this._getMarks();
    return marks.length > 0 ? Math.min(...marks) : null;
  }
}

// Example usage
(async () => {
  let student = new StudentMarksCollector("Taaher");
  await student.getSubjects();
  await student.collectMarks();
  student.displayStudentInfo();

  console.log("Highest Mark:", student.highestMark());
  console.log("Lowest Mark:", student.lowestMark());

  rl.close(); // close input stream
})();
