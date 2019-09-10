// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

function cleanString(str) {
  return str.replace(/[^\w]/g, '').toLowerCase().split('').sort().join('');
}

function anagrams(stringA, stringB) {
  return cleanString(stringA) === cleanString(stringB)
}
// console.log(anagrams('hello', 'llohe'))
module.exports = anagrams;


// function getCharCount(str) {
//   charCount = {};
//   str = str.replace(' ', '');
//   str = str.replace(/[^\w]/g, '').toLowerCase();
//   for (let char of str) {
//     charCount[char] = charCount[char] ? charCount[char] + 1 : 1;
//   }
//   return charCount
// }

// function anagrams(stringA, stringB) {
//   charCountA = getCharCount(stringA)
//   charCountB = getCharCount(stringB)
  
//   if(Object.keys(charCountA).length !== Object.keys(charCountB).length) {
//     return false
//   } else {
//     keys = Object.keys(charCountA)
//     for (let k of keys) {
//       if (charCountA[k] !== charCountB[k]) {
//         return false
//       }
//     return true
//     }
//   }
// }