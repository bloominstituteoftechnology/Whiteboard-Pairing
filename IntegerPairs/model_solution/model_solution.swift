/*
Naive, brute force implementation.
O(n^2) runtime O(1) space
*/
func integerPairs(in array: [Int], summingTo k: Int) {
	for (i, number) in array.enumerated() {
		for number2 in array.dropFirst(i) where
		number2 == k - number {
			print("\(number2) \(number)")
		}
	}
}

/* 
	A runtime-efficient implemention that
	trades time efficiency for space efficiency

	O(n) runtime with O(n) space
*/
func integerPairs2(in array: [Int], summingTo k: Int) {
	// Use a set (hash-table) to store key-value pairs of numbers
	var seen = Set<Int>()
	for number in array {
		// check to see if the complement for the
		// current element exists in the hash
		if seen.contains(k - number) {
			print(number, k - number)
		} else {
			// If not, add this number to the set
			seen.insert(number)
		}
	}
}

/*
	An alternative implementation that favors
	memory efficiency over time efficiency

	O(n log n) runtime due to the sorting
	with O(1) space
*/
extension Array where Element == Int {
	mutating func integerPairs(summingTo k: Int) {
		// Sort the array in-place, avoiding a copy
		sort() 
		// initialize indices to track both ends of the array
		var first = startIndex
		var last = endIndex.advanced(by: -1)
		
		while first < last {
			let sum = self[first] + self[last]
			// check to see if the two elements sum up to k
			if sum == k {
				print("\(self[first]) \(self[last])")
				first = first.advanced(by: 1)
				last = last.advanced(by: -1)
			} else {
				// if they don't then we decide whether we increment
				// the first index or decrement the last index
				if sum < k {
					first = first.advanced(by: 1)
				} else {
					last = last.advanced(by: -1)
				} 
			}
		}
	}
}

let variant = integerPairs2
variant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11);  // should print '6 5', '7 4', '8 3', '9 2', '10 1'
variant([5, 5, 4], 12);                        // should not print anything
variant([99, 45, 38, 1, 68, 78], 100);         // should print '1 99'
