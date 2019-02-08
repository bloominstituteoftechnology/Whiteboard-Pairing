"""
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
"""

def is_binary_search_tree(root):
  # start at the root, with an arbitrarily low lower bound
  # and an arbitrarily high upper bound
  node_bounds_stack = []
  node_bounds_stack.append({'node': root, 'lower': float('-inf'), 'upper': float('inf')})

  # perform a depth-first traversal
  while len(node_bounds_stack):
    node_bounds = node_bounds_stack.pop()
    node = node_bounds['node']
    lower = node_bounds['lower']
    upper = node_bounds['upper']

    # if this node is invalid, return False right away
    if node.value <= lower or node.value >= upper:
      return False
    
    if node.left:
      # this node must be less than the current node
      node_bounds_stack.append({'node': node.left, 'lower': lower, 'upper': node.value})

    if node.right:
      # this node must be greater than the current node
      node_bounds_stack.append({'node': node.right, 'lower': node.value, 'upper': upper}) 
    
  return True


class BinaryTreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert_left(self, value):
    self.left = BinaryTreeNode(value)
    return self.left

  def insert_right(self, value):
    self.right = BinaryTreeNode(value)
    return self.right

# Some print tests
root = BinaryTreeNode(50)
root.insert_left(30)
root.left.insert_left(20)
root.left.insert_right(60)
root.insert_right(80)
root.right.insert_left(70)
root.right.insert_right(90)

print(is_binary_search_tree(root.left))  # should print True
print(is_binary_search_tree(root.right)) # should print True
print(is_binary_search_tree(root))       # should print False