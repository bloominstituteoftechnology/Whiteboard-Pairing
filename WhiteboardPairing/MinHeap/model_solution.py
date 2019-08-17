# An implementation that uses a storage array as the backing
# for the min heap. In order to emulate a binary tree structure,
# we have the following rules:

# 1. We can calculate a parent node's left child with the
#    formula `index * 2 + 1`.
# 2. We can calculate a parent node's right child with the
#    formula `index * 2 + 2`.
# 3. Given the index of a child node, the formula to 
#    calculate the child's parent's index is
#    `Math.floor((index - 1) / 2)`.

# Using these forumulas, we can swap the values of parent nodes 
# that are greater then their children node's values and vice versa.

class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # push the given value to the end of the storage array
        self.storage.append(value)
        # use the `_bubbleUp` method to move this new value to
        # a valid spot in the min heap
        self._bubbleUp(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) == 0:
            return
        if len(self.storage) == 1:
            return self.storage.pop()

        minValue = self.storage[0]
        # overwrite the old min value at the root of
        # the heap with the last value in the heap
        self.storage[0] = self.storage.pop()
        # call `_siftDown` to move the new value at the root
        # of the heap to a valid spot, making way for the
        # proper root of the min heap
        self._siftDown(0)
        return minValue

    def getMin(self):
        if len(self.storage) == 0:
            return None
        return self.storage[0]


    # helper method that checks to see if the value at the given index
    # is in a valid spot in the heap if it isn't, the value will
    # be swapped with its parent's value until it reaches a valid spot
    def _bubbleUp(self, index):
        if index <= 0:
            return
        parentIndex = (index - 1) // 2
        if self.storage[parentIndex] > self.storage[index]:
            swap = self.storage[index]
            self.storage[index] = self.storage[parentIndex]
            self.storage[parentIndex] = swap
            self._bubbleUp(parentIndex)

    # helper method that checks to see if the value at the given index
    # is in a valid spot in the heap if it isn't, the value will
    # be swapped with its smallest child's value until it reaches a valid spot
    def _siftDown(self, index):
        leftChildIndex = index * 2 + 1
        rightChildIndex = index * 2 + 2

        if leftChildIndex < len(self.storage) and rightChildIndex < len(self.storage):
            if self.storage[leftChildIndex] < self.storage[rightChildIndex]:
                minChildIndex = leftChildIndex
            else:
                minChildIndex = rightChildIndex
        elif leftChildIndex < len(self.storage):
            minChildIndex = leftChildIndex
        else:
            minChildIndex = rightChildIndex

        if minChildIndex >= len(self.storage):
            return

        if self.storage[index] > self.storage[minChildIndex]:
            swap = self.storage[minChildIndex]
            self.storage[minChildIndex] = self.storage[index]
            self.storage[index] = swap
            self._siftDown(minChildIndex)

heap = Heap()
print(heap.getMin())    # should print None

heap.insert(5)
print(heap.getMin())   # should print 5

heap.insert(100)
print(heap.getMin())   # should print 5

heap.insert(2)
print(heap.getMin())   # should print 2

print(heap.delete())   # should print 2
print(heap.delete())   # should print 5
print(heap.delete())   # should print 100

print(heap.getMin())   # should print 'undefined'


