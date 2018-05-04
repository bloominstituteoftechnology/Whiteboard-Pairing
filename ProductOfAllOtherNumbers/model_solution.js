/* 
  How would you solve this problem if division was allowed?
*/
function getProductsOfAllIntsExceptAtIndex(intArray) {
  if (intArray.length < 2) {
    throw new Error('Getting the product of numbers at other indices requires at least 2 numbers');
  }
  
  const productsOfAllIntsExceptAtIndex = [];
  
  // For each integer, we find the product of all the integers
  // before it, storing the total product so far each time
  let productSoFar = 1;
  for (let i = 0; i < intArray.length; i++) {
    productsOfAllIntsExceptAtIndex[i] = productSoFar;
    productSoFar *= intArray[i];
  }
  
  // For each integer, we find the product of all the integers
  // after it. Since each index in products already has the
  // product of all the integers before it, now we're storing
  // the total product of all other integers
  productSoFar = 1;
  for (let j = intArray.length - 1; j >= 0; j--) {
    productsOfAllIntsExceptAtIndex[j] *= productSoFar;
    productSoFar *= intArray[j];
  }

  return productsOfAllIntsExceptAtIndex;
};

/* Some console.log tests */
console.log(getProductsOfAllIntsExceptAtIndex(
  [1, 2, 3, 4, 5]
));   // should print [120, 60, 40, 30, 24]

console.log(getProductsOfAllIntsExceptAtIndex(
  [9, 90]
));   // sould print [90, 9]