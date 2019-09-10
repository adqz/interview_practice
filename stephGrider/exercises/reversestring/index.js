// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {
  arr = str.split('');
  rev = arr.reduce( (reversed, char) => char + reversed, '')
  return rev;
}

console.log(reverse('madam im adam'))
module.exports = reverse;



// function reverse(str) {
//   arr = str.split('');
//   rev = ''
//   for(let char of arr) {
//     rev = char + rev;
//   }
//   return rev
// }

// function reverse(str) {
//   return str.split('').reverse().join('');
// }