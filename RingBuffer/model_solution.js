class RingBuffer {
  constructor(capacity) {
    this.capacity = capacity;
    this.current = 0;
    this.storage = [];
  }

  append(item) {
    this.storage[this.current++] = item;
    // If we reach the capacity of the buffer
    // set the current pointer back to the beginning
    if (this.current === this.capacity) {
      this.current = 0;
    }
  }

  allValues() {
    return this.storage;
  }
}

/* Some console.log tests */
const buffer = new RingBuffer(5);

buffer.append('a');
buffer.append('b');
buffer.append('c');
buffer.append('d');
console.log(buffer.allValues());  // should print ['a', 'b', 'c', 'd']

buffer.append('e');
console.log(buffer.allValues());  // should print ['a', 'b', 'c', 'd', 'e']

buffer.append('f');
console.log(buffer.allValues());  // should print ['f', 'b', 'c', 'd', 'e']

buffer.append('g');
buffer.append('h');
buffer.append('i');
console.log(buffer.allValues());  // should print ['f', 'g', 'h', 'i', 'e']