/*
  The strategy here is to do a depth-first traversal of 
  the tree, checking for validity as we go. A node is valid
  if it is greater than all its ancestor nodes . We also 
  to check that, if the node is in the left subtree, that 
  is less than all the right nodes in the right subtree. 
  Conversely, we need to check that all the nodes in the
  right subtree are greater than the nodes in the left subtree.

  Instead of keeping track of each ancestor, though, we can
  just check the largest number it must be greater than and 
  the smallest number it must be less than.
*/

function isBinarySearchTree(root) {
  // start at the root, with an arbitrarily low lower bound
  // and an arbitrarily high upper bound
  const nodeAndBoundsStack = [];
  nodeAndBoundsStack.push({node: root, lowerBound: -Infinity, upperBound: Infinity});

  // depth-first traversal
  while (nodeAndBoundsStack.length) {
    const nodeAndBounds = nodeAndBoundsStack.pop();
    const node = nodeAndBounds.node;
    const lowerBound = nodeAndBounds.lowerBound;
    const upperBound = nodeAndBounds.upperBound;

    // if this node is invalid, we return false right away
    if (node.value <= lowerBound || node.value >= upperBound) {
        return false;
    }

    if (node.left) {
      // this node must be less than the current node
      nodeAndBoundsStack.push({node: node.left, lowerBound: lowerBound, upperBound: node.value});

    }
    if (node.right) {
      // this node must be greater than the current node
      nodeAndBoundsStack.push({node: node.right, lowerBound: node.value, upperBound: upperBound});
    }
  }

  return true;
}

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

/* Some console.log tests */
const root = new BinaryTreeNode(50);
root.insertLeft(30);
root.left.insertLeft(20);
root.left.insertRight(60);
root.insertRight(80);
root.right.insertLeft(70);
root.right.insertRight(90);

console.log(isBinarySearchTree(root.left));   // should print true
console.log(isBinarySearchTree(root.right));  // should print true
console.log(isBinarySearchTree(root));        // should print false