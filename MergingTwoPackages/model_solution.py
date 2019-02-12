

def getIndicesOfItemWeights(arr, limit):

  # use a dictionary to store item weights
  # along with their 'complement'
  o = {}

  for i in range(len(arr)):
      weight = arr[i]
      # check the object to see if we have the
      # complement of the current weight
      complement = limit - weight
      if complement in o:
          # If we do, then we're done!
          return [i, o[complement]]
      else:
          # otherwise, store the weight with its index
          o[weight] = i
  return []

print(getIndicesOfItemWeights(
  [4, 6, 10, 15, 16],
  21
))   # should print [3, 1]

print(getIndicesOfItemWeights(
  [4, 4],
  8
))   # should print [1, 0]

print(getIndicesOfItemWeights(
  [12, 6, 7, 14, 19, 3, 0, 25, 40],
  7
))   # should print [6, 2]

print(getIndicesOfItemWeights(
  [9],
  9
))   # should print []