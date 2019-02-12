/*
  I would recommend diagraming this algorithm
  out. It will make a lot more sense that way.
*/

// s is an input Stack
function sortStack(s) {
  // initialize an output stack that will
  // hold all the sorted elements
  const r = new Stack();
  // we're going to keep sorting until the
  // input stack is completely empty
  while (!s.isEmpty()) {
    const temp = s.pop();
    // while our output stack still has elements
    // and the top element is larger than the 
    // value in the temp variable
    while (!r.isEmpty() && r.peek() > temp) {
      // pop off our output stack back into 
      // the input stack
      s.push(r.pop());
    }

    r.push(temp);
  }

  return r;
}


class Stack {
  constructor() {
    this.storage = [];
  }

  push(item) {
    this.storage.push(item);
  }

  pop() {
    return this.storage.pop();
  }

  peek() {
    return this.storage[this.storage.length-1];
  }

  isEmpty() {
    return this.storage.length === 0;
  }

  printContents() {
    this.storage.forEach(elem => console.log(elem));
  }
}

/* Some console.log tests */
const s = new Stack();
s.push(10);
s.push(4);

let sortedStack = sortStack(s); // sortedStack is also a Stack instance
sortedStack.printContents();    // should print 4, 10

// print a newline
console.log();

s.push(8);
s.push(5);
s.push(1);
s.push(6);
s.push(19);
s.push(4);

sortedStack = sortStack(s);
sortedStack.printContents();  // should print 1, 4, 5, 6, 8, 19