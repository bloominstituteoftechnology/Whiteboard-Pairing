# Make sure that an empty tree return True


def checkBalance(rootnode):
    if rootnode == None:
        return True
# Find the depth of the minimum tree.

    def minDepth(node):
        if node == None:
            return 0
    # RECURSION
        return 1 + min(minDepth(node.left), minDepth(node.right))
# Find the depth of the maximum tree.

    def maxDepth(node):
        if node == None:
            return 0
    # RECURSION
        return 1 + max(maxDepth(node.left), maxDepth(node.right))

# If the maxdepth - mindepth == 0 , return true, else return false.
    return maxDepth(rootnode) - minDepth(rootnode) == 0
    # Really can return the statement, since that will be true or false.


# def checkBalance(rootnode):
#     if rootnode == None:
#         return True

#     def minDepth(node):
#         if node == None:
#             return 0
#         return 1 + min(minDepth(node.left), minDepth(node.right))

#     def maxDepth(node):
#         if node == None:
#             return 0
#         return 1 + max(maxDepth(node.left), maxDepth(node.right))

#     return maxDepth(rootnode) - minDepth(rootnode) == 0


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
print(checkBalance(root))   # should print True

root.insertLeft(10)
print(checkBalance(root))   # should print False

root.insertRight(11)
print(checkBalance(root))   # should print True
