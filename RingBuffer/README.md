# Ring Buffer

Like arrays that you saw in C, a ring buffer is a non-growable buffer with a fixed size. In this case, however, that turns out to be a feature of the data structure.

When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data. 

Implement this behavior in the `RingBuffer` class. `RingBuffer` has two methods, `append` and `get`. The `append` method adds elements to the buffer. The `get` method returns all of the elements in the buffer ordered from oldest to newest. In other words, least-recently added elements first, then most-recently added elements. 

For example:
```js
const buffer = new RingBuffer(3);

buffer.append('a');
buffer.append('b');
buffer.append('c');

buffer.get();   // should return ['a', 'b', 'c']

buffer.append('d');

buffer.get();   // should return ['d', 'b', 'c']

buffer.append('e');
buffer.append('f');

buffer.get();   // should return ['d', 'e', 'f']
```

Analyze the time and space complexity of your implementation.

