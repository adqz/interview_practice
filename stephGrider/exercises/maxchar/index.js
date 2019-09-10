// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function getCharCount1 (str) {
  charCount = {}
  for(let char of str) {
    charCount[char] = charCount[char] ? charCount[char]+1 : 1
  }
  return charCount
}
function getMaxChar(charCount) {
  let max = 0, maxChar = '';
  for (let char in charCount) {
    if (charCount[char] > max) {
      max = charCount[char]
      maxChar = char
    }
  }
  return maxChar
}
function maxChar(str) {
  charCount = getCharCount1(str);
  return getMaxChar(charCount)
}
maxChar('adnan')
module.exports = maxChar;


// function getCharCount2 (str) {
//   charCount = {};
//   for( let char of str) {
//     charCount[char] = charCount[char]+1 || 1
//   }
//   return charCount
// }

// function getCharCount3 (str) {
//   charCount = {};
//   for( let char of str) {
//     if(!charCount[char]) {
//       charCount[char] = 1
//     } else {
//       charCount[char] ++
//     }
//   }
//   return charCount
// }