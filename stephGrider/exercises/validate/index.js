// --- Directions
// Given a node, validate the binary search tree,
// ensuring that every node's left hand child is
// less than the parent node's value, and that
// every node's right hand child is greater than
// the parent

function validate(node, min = null, max = null) {
  if (max !== null && node.data > max) {
    return false
  }
  if (min !== null && node.data < min) {
    return false
  }

  if (node.left && !validate(node.left, min, node.data)) {
    return false
  }
  if (node.right && !validate(node.right, node.data, max)) {
    return false
  }

  return true
}

module.exports = validate;

// function validate(node, min = null, max = null) {
//   //base cases
//   if (!node.left && !node.right) { //no more nodes below
//     return true;
//   } else if (!node.left && node.right.data > node.data) { //only right node below
//     return true;
//   } else if (!node.right && node.left.data < node.data) { //only left node below
//     return true;
//   }
  
//   if (node.left.data < node.data && node.left.data < max) {
//     if (node.right.data > node.data && node.right.data > min) {
//       validate(node.left, null, node.data) && validate(node.right, node.data, null)
//     }
//   }

// }