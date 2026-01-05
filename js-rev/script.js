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

