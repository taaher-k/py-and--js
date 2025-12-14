//1.1

console.log("hello"+" world"); // hello world

let fruits =["apple","banana","cherry"];

process.stdout.write("bat");
process.stdout.write("man\n");


console.log(fruits.join(" ** ")); // apple ** banana ** cherry


//separator \n 
console.log(fruits.join("\n"));

// apple
// banana
// cherry

//1.2


var mydetails = ["taaher","B.com ComputerApplication",2023,]

 var name = mydetails[0]
 var course = mydetails[1]
 var year = mydetails[2]

console.log(`Name: ${name}\nCourse: ${course}\nYear of passing: ${year}`)


var a = 5;
var b = 3;

console.log (`all the arithmatic operations of a and b are:\n
Addition: ${a+b}\n
Subtraction: ${a-b}\n
Multiplication: ${a*b}\n
Division: ${a/b}\n
floor Division: ${Math.floor(a/b)}\n
Modulus: ${a%b}\n
Exponentiation: ${a**b} (eg)5x5x5=125\n
Increment: ${++a}
Decrement: ${--b}
`);


var c = b;

b = a;
a = c;
// 5 and  3  became 6 and 2 after increment and decrement
console.log(`before swapping values are:\n a = 5\n b = 3\n after swapping the values are \n a = ${a}\n b = ${b} `);

[a,b] = [b,a];

console.log(`after swapping using destructuring assignment the values are \n a = ${a}\n b = ${b}\n `);


a = a + b; // 8
b = a - b; // 5
a = a - b; // 3

console.log(`need to know this a = ${a}, b = ${b}\n`); // a = 3, b = 5


//let num = parseInt(prompt("Enter a number to check if its odd or even : "));
let num = Math.random()*10;
num = Math.floor(num);

console.log((num % 2 === 0) ?  `The number is even ${num}` : `The number is odd ${num}`);