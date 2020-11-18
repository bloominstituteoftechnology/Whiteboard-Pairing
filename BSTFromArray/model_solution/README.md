# Create a Minimal Height BST from Sorted Array

## Understanding the Problem

This problem asks us to create a valid binary search tree from a sorted array of 
integers. More specifically, the resulting binary search tree needs to be of 
_minimal height_. Our function should return the root node of the created binary
search tree. 

From the given example where the input is `[1, 2, 3, 4, 5, 6, 7]`, the expected 
answer is a binary search tree of height 3. This is the minimal height that can
be achieved for an array of 7 seven elements. Try as we might, there's no way to
construct a binary search tree containing all of these elements that has a shorter
height.

## Coming Up with a First Pass 

A straightforward way to do this would be to take the first element of our array,
call that the root, and then iterate through the rest of our array, adding those
elements as nodes in the binary search tree. In pseudocode, that might look something
like this:

```
def create_min_height_bst(sorted_arr):
  root = BinaryTreeNode(sorted_arr[0])

  for elem in sorted_arr:
    root.insert(elem)

  return root
```


