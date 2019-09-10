// --- Directions
// Given an integer, return an integer that is the reverse
// ordering of numbers.
// --- Examples
//   reverseInt(15) === 51
//   reverseInt(981) === 189
//   reverseInt(500) === 5
//   reverseInt(-15) === -51
//   reverseInt(-90) === -9

function reverseInt(n) {
  let rev = n.toString().split('').reverse().join('');
  return parseInt(rev) * Math.sign(n);
}

// function reverseInt(n) {
//   if (n==0) {
//     return 0;
//   }
//   nSign = Math.sign(n);
//   arr = Math.abs(n).toString().split('');
//   rev = arr.reduce( (reversed, c) => c + reversed, '');
//    return (nSign==1)? parseInt(rev): -1 * parseInt(rev)
// }

console.log(reverseInt(-1234));
module.exports = reverseInt;
