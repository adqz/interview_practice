// --- Directions
// Given an array and chunk size, divide the array into many subarrays
// where each subarray is of length size
// --- Examples
// chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
// chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
// chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
// chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
// chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]

function chunk(array, size) {
  let ans = [];
  for(let i=0; i<array.length; i = i+size) {
    end = (i+size < array.length) ? i+size: array.length //not needed but  still for clarity
    ans.push(array.slice(i, end))
  }
  // console.log(ans)
  return ans
}



console.log(chunk([1, 2, 3, 4, 5], 4))
module.exports = chunk;

// function chunk(array, size) {
//   let chunked = [];
//   for (el of array) {
//     const last = chunked[chunked.length-1]
//     if(!last || last.length === size) {
//       chunked.push([el]);
//     } else {
//       last.push(el);
//     }
//   }
//   return chunked
// }