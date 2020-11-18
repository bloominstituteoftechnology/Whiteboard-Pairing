function createMinimalBST(sortedArray) {
  return createMinimalBSTHelper(sortedArray, 0, sortedArray.length - 1);
}

function createMinimalBSTHelper(sortedArray, left, right) {
  if (right < left) return null;

  const mid = Math.floor((left + right) / 2);
  const node = new BinaryTreeNode(sortedArray[mid]);

  node.left = createMinimalBSTHelper(sortedArray, left, mid - 1);
  node.right = createMinimalBSTHelper(sortedArray, mid + 1, right);

  return node;
}


class BinaryTreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

/* Helper function to validate that the created tree is a valid BST */
function isBinarySearchTree(root) {
  const nodeAndBoundsStack = [];
  nodeAndBoundsStack.push({node: root, lowerBound: -Infinity, upperBound: Infinity});
  while (nodeAndBoundsStack.length) {
    const nodeAndBounds = nodeAndBoundsStack.pop();
    const node = nodeAndBounds.node;
    const lowerBound = nodeAndBounds.lowerBound;
    const upperBound = nodeAndBounds.upperBound;
    if (node.value <= lowerBound || node.value >= upperBound) {
        return false;
    }
    if (node.left) {
      nodeAndBoundsStack.push({node: node.left, lowerBound: lowerBound, upperBound: node.value});
    }
    if (node.right) {
      nodeAndBoundsStack.push({node: node.right, lowerBound: node.value, upperBound: upperBound});
    }
  }
  return true;
}

/* Helper function to check the max height of a BST */
function maxDepth(node) {
  if (!node) return 0;
  return 1 + Math.max(maxDepth(node.left), maxDepth(node.right));
}

/* Some console.log tests */
let sortedArray = [1, 2, 3, 4, 5, 6, 7];
let bst = createMinimalBST(sortedArray);

console.log(isBinarySearchTree(bst));   // should print true
console.log(maxDepth(bst));             // should print 3

sortedArray = [4, 10, 11, 18, 42, 43, 47, 49, 55, 67, 79, 89, 90, 95, 98, 100];
bst = createMinimalBST(sortedArray);

console.log(isBinarySearchTree(bst));   // should print true
console.log(maxDepth(bst));             // should print 5
