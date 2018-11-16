# Merging Two Packages

Given a package with a weight limit `limit` and an array `arr` of item weights, implement a function `getIndicesOfItemWeights` that finds two items whose sum of weights equals the weight limit limit. Your function should return a pair `[i, j]` of the indices of the item weights, ordered such that `i > j`. If such a pair doesn’t exist, return an empty array.

Analyze the time and space complexities of your solution.

Example:

**JavaScript**:

```js
input: arr = [4, 6, 10, 15, 16]
       limit = 21
output: [3, 1]   // since these are the indices of 
                 // weights 6 and 15 whose sum equals 21
```

**Swift**:

```swift
print(indicesOf(itemWeights:
	[4, 6, 10, 15, 16],
	limit: 21
))   // should print [3, 1]

print(indicesOf(itemWeights:
	[4, 4],
	limit: 8
))   // should print [1, 0]

print(indicesOf(itemWeights:
	[12, 6, 7, 14, 19, 3, 0, 25, 40],
	limit: 7
))   // should print [6, 2]

print(indicesOf(itemWeights:
	[9],
	limit: 9
))   // should print nil
```
