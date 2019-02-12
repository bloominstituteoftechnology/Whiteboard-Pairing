# How would you solve this problem if division was allowed?

def getProductsOfAllIntsExceptAtIndex(intArray):
  if len(intArray) < 2:
    return ('Getting the product of numbers at other indices requires at least 2 numbers')
  
  productsOfAllIntsExceptAtIndex = [0]*len(intArray)
  
  # For each integer, we find the product of all the integers
  # before it, storing the total product so far each time
  productSoFar = 1
  for i in range(0, len(intArray)):
    productsOfAllIntsExceptAtIndex[i] = productSoFar
    productSoFar *= intArray[i]
  
  # For each integer, we find the product of all the integers
  # after it. Since each index in products already has the
  # product of all the integers before it, now we're storing
  # the total product of all other integers
  productSoFar = 1
  for j in range(len(intArray)-1, -1, -1):
    productsOfAllIntsExceptAtIndex[j] *= productSoFar
    productSoFar *= intArray[j]

  return productsOfAllIntsExceptAtIndex


# Some console.log tests 
print(getProductsOfAllIntsExceptAtIndex( [1, 2, 3, 4, 5] ))   # should print [120, 60, 40, 30, 24]
print(getProductsOfAllIntsExceptAtIndex( [9, 90] ))   # should print [90, 9]
print(getProductsOfAllIntsExceptAtIndex( [50] ))   # should print 'Getting the product of numbers at other indices requires at least 2 numbers'
