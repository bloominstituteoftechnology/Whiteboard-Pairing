class Queue {
  constructor() {
    // Stack to hold elements that get added
    this.inStack = [];
    // Stack to hold elements that are getting removed
    this.outStack = [];
  }

  enqueue(item) {
    this.inStack.push(item);
  }

  dequeue() {
    // if the outStack is empty
    // we need to populate it with inStack elements
    if (this.outStack.length === 0) {
      // empty out the inStack into the outStack
      while (this.inStack.length > 0) {
        this.outStack.push(this.inStack.pop());
      }
    }
    return this.outStack.pop();
  }

  peek() {
    // same logic as `dequeue`
    if (this.outStack.length === 0) {
      while (this.inStack.length > 0) {
        this.outStack.push(this.inStack.pop());
      }
    }
    return this.outStack[0];
  }
}

/* Some console.log tests */
const q = new Queue();
console.log(q.peek());   // should print undefined

q.enqueue(10);
console.log(q.peek());   // should print 10

q.enqueue(9);
q.enqueue(8);

console.log(q.dequeue());   // should print 10
console.log(q.dequeue());   // should print 9
console.log(q.dequeue());   // should print 8