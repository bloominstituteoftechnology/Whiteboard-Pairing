// Implement Bubble Sort

var ary = [9, 8, 7, 6, 5, 4, 3, 2, 1]

function bubbleSort(arr) { 
  for (i=arr.length - 1; i>=0; i--) {
    for (j=0; j<i; j++) {
      if (arr[j] > arr[j + 1]) {
        var temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
      }
    }
  }
  return arr
}

bubbleSort(ary)