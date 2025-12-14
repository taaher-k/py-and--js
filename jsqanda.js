//1 

function reverseString(str) {
  return str.split('').reverse().join('');
}

 // "olleh"  

console.log(reverseString("hello"));
//2


function isEven(num) {
  return num % 2 === 0;
}


console.log(isEven(4));  // true
console.log(isEven(7));  // false
//3
function largest(arr) {
  return Math.max(...arr);
}
console.log(largest([1, 3, 2]));  // 3

//4
function isPalindrome(str) {
  const rev = str.split('').reverse().join('');
  return str === rev;
}
console.log(isPalindrome("racecar"));  // true
console.log(isPalindrome("hello"));    // false

//5

function countVowels(str) {
  return str.match(/[aeiou]/gi)?.length || 0;
}
console.log(countVowels("hello"));  // 2
console.log(countVowels("xyz"));    // 0

//6
function removeDuplicates(arr) {
  return [...new Set(arr)];
}
console.log(removeDuplicates([1, 2, 2, 3]));  // [1, 2, 3]


function sumArray(arr) {
  return arr.reduce((a, b) => a + b, 0);
}
console.log(sumArray([1, 2, 3, 4]));  // 10

arr = [1, 2, 3, 4];
let sum = 0;
for (const n of arr) sum += n;
    return console.log(sum);  // 10


//7

function factorial(n){ if(n===0) return 1; return n * factorial(n-1); }
 console.log(factorial(5));

//8

