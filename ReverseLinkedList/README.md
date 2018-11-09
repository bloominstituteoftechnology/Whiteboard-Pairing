# Reverse a Linked List

Write a function `reverseLinkedList` that receives a linked list node as input and then reverses the list, starting from the given node. Do this in-place without using any extra memory. Your function should return the
value of the new head of the list. 

Here is a simple Linked List class:

JavaScript:

```js
class ListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}
```

Swift:

```swift
class ListNode<T> {

	var value: T?
	var next: ListNode?
	
	init(value: T?) {
		self.value = value
		self.next = nil
	}
}
```

Analyze the time and space complexity of your solution. 