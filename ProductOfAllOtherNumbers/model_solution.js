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
 
));   // sould print [90, 9]

//Solution number 2

let testArray = [1, 7, 3, 4];

function returnProduct(array) {
  if (array.length < 2) {
    throw new Error("you need an array of at least 2 numbers to proceed.");
  }

  //map over array, multiplying each number by the all of the other numbers
  let resultsArray = array.map((num, index) => {
    let tempArray = array.slice(); //copy the original array
    tempArray.splice(index, 1); //splice the array without current integer
    const product = tempArray.reduce((acc, val) => {
      //use reduce to multiply the array values together
      return acc * val;
    });
    return product; //return the product of all array values
  });
  return resultsArray; //return the array of products
}

returnProduct(testArray);

console.log(returnProduct([1, 2, 3, 4, 5]));
console.log(returnProduct([9, 90]));

console.log(returnProduct([]));


