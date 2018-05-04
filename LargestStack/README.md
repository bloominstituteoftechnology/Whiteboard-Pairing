# Largest Stack

Assume we have a Stack class given by the following code:

```js
class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    this.items.push(item);
  }

  pop() {
    if (this.items.length) {
      return this.items.pop();
    }
    return null;
  }

  peek() {
    if (this.items.length) {
      return this.items[this.items.length-1];
    }
    return null;
  }
}
```

We wish to augment this Stack class such that we can always fetch the max value from the Stack in constant time. 

Use the given Stack class to implement a new `MaxStack` class that has all the same methods as the base Stack class, along with a `getMax` method that returns the max value of the MaxStack in O(1) time. `getMax` should not remove the item.

Analyze the time and space complexity of the methods of your MaxStack class. What tradeoffs had to occur in order for you to achieve O(1) retrieval of the maximum value?