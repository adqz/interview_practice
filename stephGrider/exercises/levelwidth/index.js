// --- Directions
// Given the root node of a tree, return
// an array where each element is the width
// of the tree at each level.
// --- Example
// Given:
//     0
//   / |  \
// 1   2   3
// |       |
// 4       5
// Answer: [1, 3, 2]

function levelWidth(root) {
  let buffer = [root, 's'];
  let widthCounter = [0];

  while(buffer.length > 1) {
    const node = buffer.shift()
    if (node !== 's') {
      widthCounter[widthCounter.length-1]++;
      buffer.push(...node.children)
    } else {
      widthCounter.push(0);
      buffer.push('s')
    }
  }
  return widthCounter
}

module.exports = levelWidth;


// function levelWidth(root) {
//   const stopper = new Node('stop')
//   let buffer = [root, stopper];
//   let widthCounter = [];
//   let counter = 0

//   while(buffer.length) {
//     let node = buffer.shift();
//     if (node.data === 'stop') {
//       widthCounter.push(counter)
//       counter = 0;
//       if (!buffer.length) { //to check if we reached end of tree
//         break;
//       }
//       buffer.push(stopper)
//     } else {
//       counter ++;
//       buffer.push(...node.children)
//     }
//   }
//   return widthCounter;
// }