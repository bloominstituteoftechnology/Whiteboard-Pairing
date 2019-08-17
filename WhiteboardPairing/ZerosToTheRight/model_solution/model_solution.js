function zerosToTheRight(arr) {
    let left = 0;
    let right = arr.length - 1;
    let nZeros = 0;

    while (left <= right) {
        if (arr[left] === 0 && arr[right] !== 0) {
            [arr[left], arr[right]] = [arr[right], arr[left]];
            left++;
            right--;
            nZeros++;
        } else {
            if (arr[left] !== 0) {
                left++;
            }
            if (arr[right] === 0) {
                right--;
                nZeros++;
            }
        }
    }

    console.log(arr);
    return arr.length - nZeros;
}

// function zerosToTheRight(arr) {
//     let nonZero = 0;
// 
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] !== 0) {
//             [arr[i], arr[nonZero]] = [arr[nonZero], arr[i]];
//             nonZero++;
//         }
//     }
// 
//     console.log(arr);
//     return nonZero;
// }

console.log("Number of non-zero integers: ", zerosToTheRight([0, 3, 1, 0, -2]));
// should print:
// [-2, 3, 1, 0, 0]
// Number of non-zero integers: 3

console.log("Number of non-zero integers: ", zerosToTheRight([1, 2, 3, 0, 4, 0, 0]));
// should print:
// [1, 2, 3, 4, 0, 0, 0]
// Number of non-zero integers: 4

console.log("Number of non-zero integers: ", zerosToTheRight([4, 1, 2, 5]));
// should print:
// [4, 1, 2, 5]
// Number of non-zero integers: 4

console.log("Number of non-zero integers: ", zerosToTheRight([0, 0, 0, 0, 0]));
// should print:
// [0, 0, 0, 0, 0]
// Number of non-zero integers: 0

console.log("Number of non-zero integers: ", zerosToTheRight([0, 0, 0, 0, 3, 2, 1]));
// should print:
// [1, 2, 3, 0, 0, 0, 0]
// Number of non-zero integers: 3

