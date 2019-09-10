// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

function vowels(str) {
  matches = str.match(/[aeiou]/gi); //g tells it to not stop at first match and i tells it to be insensitive to case
  return matches ? matches.length : 0
}
console.log(vowels('bcdfghjkl'))
module.exports = vowels;

// function vowels(str) {
//   letters = str.replace(/[^\w]/g, '').toLowerCase().split('')
//   allVowels = ['a', 'e', 'i', 'o', 'u']
//   var count = 0;
//   for (let char of letters) {
//     count = allVowels.includes(char) ? count+1: count
//   }
//   return count
// }