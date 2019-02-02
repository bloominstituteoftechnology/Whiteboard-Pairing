import math

def create_minimal_BST(sorted_array):
    return create_minimal_BST_helper(sorted_array, 0, len(sorted_array) - 1)

def create_minimal_BST_helper(sorted_array, left, right):
    if right < left:
        return None

    mid = math.floor((left + right) / 2)
    node = BinaryTreeNode(sorted_array[mid])

    node.left = create_minimal_BST_helper(sorted_array, left, mid - 1)
    node.right = create_minimal_BST_helper(sorted_array, mid + 1, right)

    return node

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Helper function to validate that the created tree is a valid BST
def is_BST(root):
    node_and_bounds_stack = []
    node_and_bounds_stack.append({"node": root, "lower_bound": -math.inf, "upper_bound": math.inf})

    while node_and_bounds_stack != []:
        node_and_bounds = node_and_bounds_stack.pop()
        node = node_and_bounds["node"]

        lower_bound = node_and_bounds["lower_bound"]
        upper_bound = node_and_bounds["upper_bound"]

        if node.value <= lower_bound or node.value >= upper_bound:
            return False

        if node.left != None:
            node_and_bounds_stack.append({"node": node.left, "lower_bound": lower_bound, "upper_bound": node.value})

        if node.right != None:
            node_and_bounds_stack.append({"node": node.right, "lower_bound": node.value, "upper_bound": upper_bound})

    return True

# Helper function to check the max height of a BST
def max_depth(node):
    if node == None: return 0

    return 1 + max(max_depth(node.left), max_depth(node.right))

# Some tests
sorted_array = [1, 2, 3, 4, 5, 6, 7]
bst = create_minimal_BST(sorted_array)

print(is_BST(bst))     # should print true
print(max_depth(bst))  # should print 3

sorted_array = [4, 10, 11, 18, 42, 43, 47, 49, 55, 67, 79, 89, 90, 95, 98, 100]
bst = create_minimal_BST(sorted_array)

print(is_BST(bst))     # should print true
print(max_depth(bst))  # should print 5
