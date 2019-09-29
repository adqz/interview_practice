// --- Directions
// Write a function that accepts a string.  The function should
// capitalize the first letter of each word in the string then
// return the capitalized string.
// --- Examples
//   capitalize('a short sentence') --> 'A Short Sentence'
//   capitalize('a lazy fox') --> 'A Lazy Fox'
//   capitalize('look, it is working!') --> 'Look, It Is Working!'

function capitalize(str) {
  words = str.
    split(' ').
    reduce( (sentence, word) => sentence + word[0].toUpperCase() + word.slice(1) + ' ', '').
    trim()
  
  return words
}
capitalize('a short sentence');
capitalize('look, it is working!');
module.exports = capitalize;

// function capitalize(str) {
//   words = str.split(' ')
//   capitalizedWords = []
//   for (let word of words) {
//     word = word[0].toUpperCase() + word.slice(1)
//     capitalizedWords.push(word)
//   }
//   return capitalizedWords.join(' ')
// }


// function capitalize(str) {
//   ans = str[0].toUpperCase()
//   for (let i=1; i<str.length; i++) {
//     if (str[i-1] === ' ') {
//       ans += str[i].toUpperCase();
//     } else {
//       ans += str[i];
//     }
//   }
//   return ans;
// }