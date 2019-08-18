#  A recursive solution
#  How would you solve this iteratively?

def checkBalanced(rootNode):
    # An empty tree is balanced by default
    if rootNode == None:
        return True

    # recursive helper function to check the min depth of the tree
    def minDepth(node):
        if node == None:
            return 0
        return 1 + min(minDepth(node.left), minDepth(node.right))

    # recursive helper function to check the max depth of the tree
    def maxDepth(node):
        if node == None:
            return 0
        return 1 + max(maxDepth(node.left), maxDepth(node.right))
    
    return maxDepth(rootNode) - minDepth(rootNode) == 0;

# Some console.log tests
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insertRight(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

root = BinaryTreeNode(5)
print(checkBalanced(root))   # should print True

root.insertLeft(10)
print(checkBalanced(root))   # should print False

root.insertRight(11)
print(checkBalanced(root))   # should print True