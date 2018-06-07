/*
  An implementation that uses a storage array as the backing
  for the min heap. In order to emulate a binary tree structure,
  we have the following rules:

  1. We can calculate a parent node's left child with the
     formula `index * 2 + 1`.
  2. We can calculate a parent node's right child with the
     formula `index * 2 + 2`.
  3. Given the index of a child node, the formula to 
     calculate the child's parent's index is
     `Math.floor((index - 1) / 2)`.

  Using these forumulas, we can swap the values of parent nodes 
  that are greater then their children node's values and vice versa.
*/
class Heap {
  constructor() {
    this.storage = [];
  }

  insert(value) {
    // push the given value to the end of the storage array
    const index = this.storage.push(value) - 1;
    // use the `_bubbleUp` method to move this new value to
    // a valid spot in the min heap
    this._bubbleUp(index);
  }

  delete() {
    if (!this.storage.length) return;
    if (this.storage.length === 1) {
      return this.storage.pop();
    }

    const min = this.storage[0];
    // overwrite the old min value at the root of 
    // the heap with the last value in the heap
    this.storage[0] = this.storage.pop();
    // call `_siftDown` to move the new value at the root
    // of the heap to a valid spot, making way for the
    // proper root of the min heap
    this._siftDown(0);
    return min;
  }

  getMin() {
    return this.storage[0];
  }
  // helper method that checks to see if the value at the given index
  // is in a valid spot in the heap; if it isn't, the value will 
  // be swapped with its parent's value until it reaches a valid spot
  _bubbleUp(index) {
    const parentIndex = Math.floor((index - 1) / 2);
    if (this.storage[parentIndex] > this.storage[index]) {
      [this.storage[parentIndex], this.storage[index]] = [this.storage[index], this.storage[parentIndex]];
      this._bubbleUp(parentIndex);
    }
  }
  // helper method that checks to see if the value at the given index
  // is in a valid spot in the heap; if it isn't, the value will 
  // be swapped with its smallest child's value until it reaches a valid spot
  _siftDown(index) {
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;
    let minChildIndex;

    if (this.storage[leftChildIndex] && this.storage[rightChildIndex]) {
      minChildIndex = this.storage[leftChildIndex] < this.storage[rightChildIndex] ? leftChildIndex : rightChildIndex;
    } else if (this.storage[leftChildIndex]) {
      minChildIndex = leftChildIndex;
    } else if (this.storage[rightChildIndex]) {
      minChildIndex = rightChildIndex;
    }

    if (this.storage[index] > this.storage[minChildIndex]) {
      [this.storage[minChildIndex], this.storage[index]] = [this.storage[index], this.storage[minChildIndex]];
      this._siftDown(minChildIndex);
    }
  }
}

/* Some console.log tests */
const heap = new Heap();
console.log(heap.getMin());    // should print 'undefined'

heap.insert(5);
console.log(heap.getMin());   // should print 5

heap.insert(100);
console.log(heap.getMin());   // should print 5

heap.insert(2);
console.log(heap.getMin());   // should print 2

console.log(heap.delete());   // should print 2
console.log(heap.delete());   // should print 5
console.log(heap.delete());   // should print 100

console.log(heap.getMin());   // should print 'undefined'
