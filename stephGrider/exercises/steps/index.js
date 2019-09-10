// --- Directions
// Write a function that accepts a positive number N.
// The function should console log a step shape
// with N levels using the # character.  Make sure the
// step has spaces on the right hand side!
// --- Examples
//   steps(2)
//       '# '
//       '##'
//   steps(3)
//       '#  '
//       '## '
//       '###'
//   steps(4)
//       '#   '
//       '##  '
//       '### '
//       '####'

function steps(n, row=0, stair='') {
  // thinking of problem as a recursive solution
  if(row===n) { //base case
    return;
  }
  if(n===stair.length) {
    console.log(stair);
    return steps(n, row+1); //recursive step for going to next stair
    // note steps() does not return anything so here return is just ending the function
  }
  stair = (stair.length<=row) ? stair+'#' : stair + ' '
  steps(n, row, stair); //recursive step for adding # or space as next character to stair 
}
module.exports = steps;


// function steps(n) {
//   for(let i=1; i<=n; i++) {
//     console.log('#'.repeat(i) + ' '.repeat(n-i))
//   }
// }

// function steps(n) {
//   // thinking of problem as a 2D matrix. This is an iterative solution
//   for (let row=1; row<=n; row++) {
//     toPrint = ''
//     for (let col=1; col<=n; col++) {
//       if(col<=row) {
//         toPrint += '#'
//       } else {
//         toPrint += ' '
//       }
//     }
//     console.log(toPrint)
//   }
// }