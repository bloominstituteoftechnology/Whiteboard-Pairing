# Depth-First Search

Implement a function `depthFirstForEach`, once as a recursive function, and then again in an iterative fashion. Your functions should receive a callback and invoke that callback on each node as it is traversing in depth-first fashion. Your functions should also receive a tree node so that it can begin traversing. 

Here is an example tree class:
```js
class BinaryTreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insertLeft(value) {
    this.left = new BinaryTreeNode(value);
    return this.left;
  }

  insertRight(value) {
    this.right = new BinaryTreeNode(value);
    return this.right;
  }
}
```

For example, given a tree like the following

                      6
                    /   \
                  10     18
                 /         \
                9           89

and the following callback function
```js
const cb = (x) => console.log(x);
```

your `depthFirstForEach` function should start at the root node and print out, in this order, 6, 10, 9, 18, 89.

Analyze the time and space complexity of your recursive and iterative solutions.