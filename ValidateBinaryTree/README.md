# Validate a Binary Tree

Given a binary tree like the following:
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

Write a function that accepts a binary tree node and returns true if the tree rooted at that node forms a valid binary search tree.

Example:
```js
const root = new BinaryTreeNode(10);
root.insertLeft(5);
root.insertRight(15);

isBinarySearchTree(root);   // should return true
```

Keep in mind that it isn't enough to check that nodes in the left subtree are always descending as we traverse down. Conversely, it isn't enough to simply check that all the nodes in the right subtee are ascending. 

We might have a tree that looks like this:

                        50
                      /    \
                    30      80
                   /  \    /  \
                  20  60  70  90

The value of 60 in the left subtree is correct if we were only considering the tree rooted at 30, however, considering the entire tree, 60 should not be in the left subtee at all, since 60 is greater than the root.

Analyze the time and space complexity of your solution.