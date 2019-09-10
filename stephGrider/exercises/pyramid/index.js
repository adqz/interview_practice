// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a pyramid shape
// with N levels using the # character.  Make sure the
// pyramid has spaces on both the left *and* right hand sides
// --- Examples
//   pyramid(1)
//       '#'
//   pyramid(2)
//       ' # '
//       '###'
//   pyramid(3)
//       '  #  '
//       ' ### '
//       '#####'
//   pyramid(4)
//      '   #   '
//      '  ###  '
//      ' ##### '
//      '#######'

  function pyramid(n, row=0, stair='') {
  /* Recursive solution */
  // Base case
  if (row === n) {
    return;
  }

  if(n===stair.length) {
    console.log(stair.split('').slice(1).reverse().join('') + stair);
    return pyramid(n, row+1); //recursive step for going to next level of pyramid
    // note pyramid() does not return anything so here return is just ending the function
  }
  stair = (stair.length<=row) ? stair+'#' : stair + ' '
  pyramid(n, row, stair); //recursive step for adding # or space as next character to pyramid
  
}
pyramid(4)
module.exports = pyramid;


// function pyramid(n) {
//   let numSpaces = n-1
//   let totalNumPounds = n + (n-1)
//   for(let numPounds=1; numPounds<=totalNumPounds; numPounds = numPounds+2) {
//     numSpaces = Math.ceil((totalNumPounds-numPounds)/2)
//     toPrint = ' '.repeat(numSpaces) + '#'.repeat(numPounds) + ' '.repeat(numSpaces)
//     console.log(toPrint)
//   }
// }


// function pyramid(n) {
//   totalNumChars = n + (n-1)
//   mid = Math.ceil(totalNumChars/2)
//   for(let row=0; row<n; row++){
//     stair=''
//     for(let col=1; col<=totalNumChars; col++) {
//       if (col<mid-row || col>mid+row) {
//         stair += ' '
//       } else {
//         stair += '#'
//       }
//     }
//     console.log(stair)
//   }
// }

// function pyramid(n, row=0, col=0, stair='') {
//   /* Recursive solution */
//   // Base case
//   if (row === n) {
//     return;
//   }

//   if(stair.length == (2*n - 1)) {
//     console.log(stair)
//     return pyramid(n, row+1)
//   }
//   mid = Math.floor((2*n-1)/2)
//   if(col < mid-row || col>mid+row) {
//     stair += ' '
//   } else {
//     stair += '#'
//   }
//   pyramid(n, row, col+1, stair)
// }


// function pyramid(n) {
//   totalNumChars = n + (n-1)
//   mid = Math.ceil(totalNumChars/2)
//   for(let row=1; row<=n; row++){
//     stair=''
//     for(let col=1; col<=mid; col++) {
//       stair = col<=row ? stair + '#' : stair + ' '
//     }
//     console.log(stair.split('').slice(1).reverse().join('') + stair)
//   }
// }