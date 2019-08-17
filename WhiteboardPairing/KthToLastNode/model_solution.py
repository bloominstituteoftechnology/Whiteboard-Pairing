# This algorithm maintains a k-wide 'window' with two pointers
# and makes one walk down the linked list. When the pointer in
# front reaches the end of the list, the second pointer will be
# at the node we're looking for.

# Another approach could be walking down the list to count the
# length of the list, subtract k from the total length, and
# then walking to that node.

# Think about some of the tradeoffs between these two approaches.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None



def kthToLastNode(k, head):
    if k < 1:
        raise Exception(f"Impossible to find less than first to last node: {k}")

    leftNode = head
    rightNode = head

    # move rightNode to the kth node
    for i in range(k - 1):
        # but along the way, if a rightNode doesn't have a next,
        # then k is greater than the length of the list and there
        # can't be a kth-to-last node! we'll raise an error
        if not rightNode.next:
            raise Exception(f"k is larger than the length of the linked list: {k}")

        rightNode = rightNode.next

    # starting with leftNode on the head,
    # move leftNode and rightNode down the list,
    # maintaining a distance of k between them,
    # until rightNode hits the end of the list
    while rightNode.next:
        leftNode = leftNode.next
        rightNode = rightNode.next


    # since leftNode is k nodes behind rightNode,
    # leftNode is now the kth to last node!
    return leftNode.value

a = ListNode("Australian Sheperd")
b = ListNode("Beagle")
c = ListNode("Cairne Terrier")
d = ListNode("Dobermann")
e = ListNode("English Mastiff")

a.next = b
b.next = c
c.next = d
d.next = e

# Some tests
print(kthToLastNode(2, a))   # should print 'Dobermann'
print(kthToLastNode(5, a))   # should print 'Australian Sheperd'
print(kthToLastNode(3, c))   # should print 'Cairne Terrier'


