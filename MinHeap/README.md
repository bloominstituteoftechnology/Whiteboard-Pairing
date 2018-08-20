# Min Heap 

A min heap is a binary tree data structure that satisfies the following property: The value of every parent node is less than or equal to the values of their direct children nodes. It follows then that the node at the root of the tree is the element in the heap with the minimal value. 

![min heap](min_heap_example.jpg)

Implement a min heap data structure with at least the following methods:

 - `insert(item)` adds the given item to the heap. Upon insertion, the heap property needs to be maintained.
 - `delete()` removes and returns the root element (the min value) of the heap. Upon deletion, the heap property needs to be maintained.
 - `getMin()` returns the minimal value of the heap in constant time. This method does not remove the minimal value from the heap.

Examples:
```js
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
```

Analyze the time and space complexity of your implementation.
