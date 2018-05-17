# Binary Search Tree from Sorted Array

Given an array that is sorted in ascending order containing unique integer elements, write a function that receives the sorted array as input and creates a valid binary search tree with minimal height.

For example, given an array `[1, 2, 3, 4, 5, 6, 7]`, your function should return a binary search tree with the form 
                          4
                        /   \
                      2       6
                     / \     / \
                    1   3   5   7

Note that when we say "binary search tree" in this case, we're just talking about a tree that exhibits the expected _form_ of a binary search tree. The tree in this case won't have an `insert` method that does the work of receiving a value and then inserting it in a valid spot in the binary search tree. Your function should place the values in valid spots that adhere to the rules of binary search trees, while also seeking to minimize the overall height of the tree.

Here's a `BinaryTreeNode` class that you can use to construct a binary search tree:
```js
class BinaryTreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
```

Analyze the time and space complexity of your solution.