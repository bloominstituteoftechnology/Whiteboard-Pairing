function createMinHeightBST(sortedArray) {
  const left = 0;
  const right = sortedArray.length - 1;

  return recHelper(sortedArray, left, right);
}

function recHelper(sortedArray, left, right) {
  if (left > right) {
    return null;
  }

  const midpoint = (math.floor((right - left)) / 2) + left;
  const root = new BinaryTreeNode(sortedArray[midpoint]);

  root.left = recHelper(sortedArray, left, midpoint - 1);
  root.right = recHelper(sortedArray, midpoint + 1, right);

  return root;
}

class BinaryTreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function isBST(root, minBound, maxBound) {
  if (root === null) {
    return true;
  }

  if (root.value < minBound || root.value > maxBound) {
    return false;
  }

  const left = isBST(root.left, minBound, root.value - 1);
  const right = isBST(root.right, root.value + 1, maxBound);

  return left && right;
}

function findBSTMaxHeight(node) {
  if (node === null) {
    return 0;
  }

  return 1 + Math.max(findBSTMaxHeight(node.left), findBSTMaxHeight(node.right));
}

function isBSTMinHeight(root, N) {
  const height = findBSTMaxHeight(root);
  const shouldEqual = Math.floor(Math.log2(N)) + 1;

  return height === shouldEqual;
}

function countBSTNodes(root, count) {
  if (root === null) {
    return count;
  }

  countBSTNodes(root.left, count);
  count++;
  countBSTNodes(root.right, count);
}

// Some tests
let sortedArray = [1, 2, 3, 4, 5, 6, 7];
let bst = createMinHeightBST(sortedArray);

console.log(isBST(bst, -Infinity, Infinity));
console.log(isBSTMinHeight(bst, sortedArray.length));

sortedArray = [4, 10, 11, 18, 42, 43, 47, 49, 55, 67, 79, 89, 90, 95, 98, 100];
bst = createMinHeightBST(sortedArray);

console.log(isBST(bst, -Infinity, Infinity));
console.log(isBSTMinHeight(bst, sortedArray.length));

