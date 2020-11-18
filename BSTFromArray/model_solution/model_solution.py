import math

def create_min_height_bst(sorted_array):
    left = 0
    right = len(sorted_array) - 1

    return rec_helper(sorted_array, left, right)
    

def rec_helper(sorted_array, left, right):
    if left > right:
        return None

    midpoint = ((right - left) // 2) + left 
    root = BinaryTreeNode(sorted_array[midpoint])

    root.left = rec_helper(sorted_array, left, midpoint - 1)
    root.right = rec_helper(sorted_array, midpoint + 1, right)

    return root 
    

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

# Helper function to validate that the created tree is a valid BST
def is_BST(root, min_bound, max_bound):
    if root is None:
        return True
    
    if root.value < min_bound or root.value > max_bound:
        return False

    left = is_BST(root.left, min_bound, root.value - 1)
    right = is_BST(root.right, root.value + 1, max_bound)

    return left and right
    

# Helper function to check the max height of a BST
def find_bst_max_height(node):
    if node is None: 
        return 0

    return 1 + max(find_bst_max_height(node.left), find_bst_max_height(node.right))


# Helper function to validate that the given BST exhibits the min height
def is_bst_min_height(root, N):
    bst_max_height = find_bst_max_height(root)
    should_equal = math.floor(math.log2(N)) + 1
    
    return bst_max_height == should_equal


# Helper function to count the number of nodes for a given BST 
def count_bst_nodes(root, count):
    if root is None:
        return count 

    count_bst_nodes(root.left, count)
    count += 1
    count_bst_nodes(root.right, count)
    

# Some tests
sorted_array = [1, 2, 3, 4, 5, 6, 7]
bst = create_min_height_bst(sorted_array)

print(is_BST(bst, float("-inf"), float("inf")))     # should print true
print(is_bst_min_height(bst, len(sorted_array)))  # should print true

sorted_array = [4, 10, 11, 18, 42, 43, 47, 49, 55, 67, 79, 89, 90, 95, 98, 100]
bst = create_min_height_bst(sorted_array)

print(is_BST(bst, float("-inf"), float("inf")))     # should print true
print(is_bst_min_height(bst, len(sorted_array)))  # should print true
