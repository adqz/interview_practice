// --- Directions
// Write a function that accepts an integer N
// and returns a NxN spiral matrix.
// --- Examples
//   matrix(2)
//     [[1, 2],
//     [4, 3]]
//   matrix(3)
//     [[1, 2, 3],
//     [8, 9, 4],
//     [7, 6, 5]]
//  matrix(4)
//     [[1,  2,  3, 4],
//     [12, 13, 14, 5],
//     [11, 16, 15, 6],
//     [10,  9,  8, 7]]

function getEmptyMatrix(n) {
  emptyMatrix = [];
  for (let i=0; i<n; i++) {
    emptyMatrix.push([])
  }
  return emptyMatrix
}

function matrix(n) {
  numOfTurns = n + n-1;
  ans = getEmptyMatrix(n)
  let startColumn = 0, endColumn = n-1;
  let startRow = 0, endRow = n-1;
  let counter = 1;
  while (startColumn <= endColumn && startRow <= endRow) {
    for (let col=startColumn; col<=endColumn; col++) { //top row
      ans[startRow][col] = counter++;
    }
    startRow++;
    for (let row=startRow; row<=endRow; row++) { //last column
      ans[row][endColumn] = counter++;
    }
    endColumn--;
    for (let col=endColumn; col>=startColumn; col--) { //last row
      ans[endRow][col] = counter++;
    }
    endRow--;
    for (let row=endRow; row>=startRow; row--) { //first column
      ans[row][startColumn] = counter++;
    }
    startColumn++;
    if (counter > (n**2 + 1)) { //checking for infinite loop
      throw new RangeError('Infinite loop');
    }
    // console.log(startRow, endRow)
    // console.log(startColumn, endColumn)
  }  
  return ans
}

console.log(matrix(4))
module.exports = matrix;
