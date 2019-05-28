function zerosToTheRight(arr) {
    let left = 0;
    let right = arr.length - 1;
    let nZeros = 0;

    while (left <= right) {
        if (arr[left] === 0 && arr[right] !== 0) {
            [arr[left], arr[right]] = [arr[right], arr[left]]
            left += 1;
            right -= 1;
            nZeros += 1;
        } else {
            if (arr[left] !== 0) {
                left += 1;
            }
            if (arr[right] === 0) {
                right -= 1;
                nZeros += 1;
            }
        }
    }

    console.log(arr);
    return arr.length - nZeros;
}

console.log("Number of non-zero integers: ", zerosToTheRight([0, 3, 1, 0, -2));
// should print:
// [-2, 3, 1, 0, 0]
// Number of non-zero integers: 3

console.log("Number of non-zero integers: ", zerosToTheRight([1, 2, 3, 0, 4, 0, 0));
// should print:
// [1, 2, 3, 4, 0, 0, 0]
// Number of non-zero integers: 4

console.log("Number of non-zero integers: ", zerosToTheRight(4, 1, 2, 5));
// should print:
// [4, 1, 2, 5]
// Number of non-zero integers: 4

console.log("Number of non-zero integers: ", zerosToTheRight([0, 0, 0, 0, 0]));
// should print:
// [0, 0, 0, 0, 0]
// Number of non-zero integers: 0

console.log("Number of non-zero integers: ", zerosToTheRight([0, 0, 0, 0, 3, 2, 1));
// should print:
// [1, 2, 3, 0, 0, 0, 0]
// Number of non-zero integers: 3

