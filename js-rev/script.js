function checkAge(){
    age = document.getElementById("ageinput").value

    if(age >= 18)
        {
            console.log('elegible to vote')}
    else{
            console.log('not elegible to vote')}
}

for (let i = 1; i <= 5; i++) {
  console.log(i);
}


let i = 1;
while (i <= 5) {
  console.log(i);
  i++;
}



// resueable function

//eg add function 

function add(a,b)
{
    return a+b;
}


console.log(add(10,2));


//arrow function 

const sub = (a,b)=>a-b;


console.log(sub(10,2));


let numbers = [10,20,30];

numbers.push(40);
numbers.pop();
numbers.length;

console.log(numbers);



let user = {
    
    name     :"Taaher",
    age      :"23",
    isStudent:true
}

console.log(user);


const fruits = ["apple", "banana", "cherry"];
fruits.forEach(x => console.log(x));
// apple, banana, cherry

numbers.push(50);

numbers.forEach(x => console.log(x,numbers.indexOf(x),numbers.length));
// 10, 20, 30,




const valueToRemove = "banana";

const index = fruits.indexOf(valueToRemove);
if (index !== -1) {  // Check if found
  fruits.splice(index, 1);  // Remove 1 item at that index
}
console.log(fruits);  // ["apple", "cherry"]



let users = [
  { name: "A", age: 20 },
  { name: "B", age: 30 }
];

// Add at end (like push)
users.splice(users.length, 0, { name: "C", age: 25 });
console.log(users); 
// [{name:"A",age:20}, {name:"B",age:30}, {name:"C",age:25}]



// Insert "New" before user "B" (index 1)
users.splice(1, 0, { name: "New", age: 22 });
console.log(users); 
// [{name:"A",age:20}, {name:"New",age:22}, {name:"B",age:30}]




let userd = { name: "Taaher", age: 25, isStudent: true };
let usersd = [
  { name: "A", age: 20 },
  { name: "B", age: 30 },
  { name: "Taaher", age: 24 }  // Duplicate exists
];

// Check if user already exists by name
if (!usersd.some(u => u.name === userd.name)) {
  usersd.push(userd);
}

console.log(usersd);  
// Only adds if "Taaher" doesn't exist already




let use = { name: "Taaher", age: 25, isStudent: true };

// Find index of existing user
const inde = users.findIndex(u => u.name === use.name);

if (inde === -1) {
  users.push(use);  // Add new
} else {
  users.splice(inde, 1, use);  // Replace existing
}

console.log(users);