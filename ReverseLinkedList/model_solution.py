def reverseLinkedList(node):
  current = node
  nextNode = None
  prevNode = None

  while current:
    # store a reference to the next list node
    # before we overwrite current.next
    nextNode = current.next

    # reverse the 'next' pointer
    current.next = prevNode

    # step forward to the next list node
    prevNode = current
    current = nextNode
  

  return prevNode.value


class ListNode:
  def __init__ (self, value):
    self.value = value
    self.next = None


a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')

a.next = b
b.next = c
c.next = d
d.next = e

# Function that prints the contents of a linked list
def printList(node):
  current = node
  
  while current:
    print(current.value)
    current = current.next
  


print(reverseLinkedList(a));  # should print 'e'
printList(e);   # should print 'e', 'd', 'c', 'b', 'a'
