class RingBuffer<T> {
	init(capacity: Int) {
		self.capacity = capacity
		self.storage = Array<T?>(repeating: nil, count: capacity)
	}
	
	func append(_ item: T) {
		storage[currentIndex] = item
		currentIndex += 1
		// If we reach the capacity of the buffer
		// set the current pointer back to the beginning
		if currentIndex == capacity {
			currentIndex = 0
		}	
	}
	
	var allValues: [T] {
		return storage.compactMap { $0 }
	}
	let capacity: Int
	
	private var currentIndex = 0
	private(set) var storage: [T?]
}

let buffer = RingBuffer<String>(capacity: 5);

buffer.append("a");
buffer.append("b");
buffer.append("c");
buffer.append("d");
print(buffer.allValues);  // should print ["a", "b", "c", "d"]

buffer.append("e");
print(buffer.allValues);  // should print ["a", "b", "c", "d", "e"]

buffer.append("f");
print(buffer.allValues);  // should print ["f", "b", "c", "d", "e"]

buffer.append("g");
buffer.append("h");
buffer.append("i");
print(buffer.allValues);  // should print ["f", "g", "h", "i", "e"]