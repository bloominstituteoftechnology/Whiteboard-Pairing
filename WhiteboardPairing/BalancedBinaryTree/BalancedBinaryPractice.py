
def checkBalance(rootnode):
    if rootnode == None:
        return True

    def minDepth(node):
        if node == 0:
            return 0
        return 1 + min(minDepth(node.left), minDepth(node.right))

    def maxDepth(node):
        if node == 0:
            return 0
        return 1 + max(maxDepth(node.left), maxDepth(node.right))

    return maxDepth(rootnode) - minDepth(rootnode) == 0
