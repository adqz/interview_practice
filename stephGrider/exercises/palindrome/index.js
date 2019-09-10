// --- Directions
// Given a string, return true if the string is a palindrome
// or false if it is not.  Palindromes are strings that
// form the same word if it is reversed. *Do* include spaces
// and punctuation in determining if the string is a palindrome.
// --- Examples:
//   palindrome("abba") === true
//   palindrome("abcdefg") === false

function getReverse1(str) {
  arr = str.split('');
  rev = '';
  for (let el of arr) {
    rev = el + rev;
  }
  return rev
}

function getReverse2(str) {
  arr = str.split('')
  rev = arr.reduce( (reversed, c) => c + reversed, '')
  return rev
}

function palindrome(str) {
  rev = getReverse2(str);
  return (rev==str) 
}

module.exports = palindrome;
