// --- Directions
// Implement bubbleSort, selectionSort, and mergeSort

function bubbleSort(arr) {
  for (let i=0; i < arr.length; i++) {
    for (let j=0; j < arr.length - (i - 1); j++) {
      if (arr[j] > arr[j+1]) {
        const temp = arr[j+1]
        arr[j+1] = arr[j]
        arr[j] = temp
      }
    }
  }
  return arr
}

function selectionSort(arr) {
  for (let i=0; i < arr.length; i++){
    let indexOfMin = i
    for (let j=i+1; j < arr.length; j++){
      if (arr[j] < arr[indexOfMin]) {
        indexOfMin = j
      }
    }
    if (i !== indexOfMin){
      const temp = arr[indexOfMin]
      arr[indexOfMin] = arr[i]
      arr[i] = temp
    }
  }

  return arr
}

function mergeSort(arr) {
  if (arr.length === 1) {
    return arr;
  }
  const midPoint = Math.floor(arr.length / 2)
  const half1 = arr.slice(0, midPoint)
  const half2 = arr.slice(midPoint)
  
  return merge(mergeSort(half1), mergeSort(half2))
}

function merge(left, right) {
  result = [];
  while (left.length && right.length) {
    if (left[0] < right[0]) {
      result.push(left.shift())
    } else {
      result.push(right.shift())
    }
  }
  result.push(...left, ...right) //order doesnt matter as either left or right will be empty
  return result
}

module.exports = { bubbleSort, selectionSort, mergeSort, merge };
