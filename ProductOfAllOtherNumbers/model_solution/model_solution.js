// Solution that makes use of division
// function ProductOfAllOthers(arr) {
//     if (arr.length < 2) {
//         return;
//     }
//     
//     const result = [];
//     const totalProduct = arr.reduce((acc, x) => acc * x);
//     
//     for (let i = 0; i < arr.length; i++) {
//         result.push(totalProduct / arr[i]);
//     }
// 
//     return result;
// }

// Solution that doesn't make use of division
function productOfAllOthers(arr) {
    if (arr.length < 2) {
        return;
    }
  
    const products = [];
  
    // For each integer, we find the product of all the integers
    // before it, storing the total product so far each time
    let productSoFar = 1;
    for (let i = 0; i < arr.length; i++) {
        products[i] = productSoFar;
        productSoFar *= arr[i];
    }
  
    // For each integer, we find the product of all the integers
    // after it. Since each index in products already has the
    // product of all the integers before it, now we're storing
    // the total product of all other integers
    productSoFar = 1;
    for (let j = arr.length - 1; j >= 0; j--) {
        products[j] *= productSoFar;
        productSoFar *= arr[j];
    }

    return products;
}

// Tests
console.log(productOfAllOthers(
  [1, 2, 3, 4, 5]
));   // should print [120, 60, 40, 30, 24]

console.log(productOfAllOthers(
  [9, 90]
));   // sould print [90, 9]

console.log(productOfAllOthers(
  [50]
));   // should print undefined
