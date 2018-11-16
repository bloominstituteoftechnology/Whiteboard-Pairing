/*
O(n) for time, O(n) for space
*/
func indicesOf(itemWeights weights: [Int], limit: Int) -> (Int, Int)? {
	var indicesByWeight = [Int : Int]()
	for (i, weight) in weights.enumerated() {
		// check the object to see we have the 
		// complement of the current weight
		if let complementIndex = indicesByWeight[limit - weight] {
			return (i, complementIndex)
		} else {
			// otherwise, store the weight with its index
			indicesByWeight[weight] = i
		}
	}
	return nil
}

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