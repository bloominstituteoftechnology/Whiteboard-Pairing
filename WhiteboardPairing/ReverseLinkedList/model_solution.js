function reverseLinkedList(node) {
  let current = node;
  let nextNode = null;
  let prevNode = null;

  while (current) {
    // store a reference to the next list node
    // before we overwrite current.next
    nextNode = current.next;

    // reverse the 'next' pointer
    current.next = prevNode;

    // step forward to the next list node
    prevNode = current;
    current = nextNode;
  }

  return prevNode.value;
}

class ListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const a = new ListNode('a');
const b = new ListNode('b');
const c = new ListNode('c');
const d = new ListNode('d');
const e = new ListNode('e');

a.next = b;
b.next = c;
c.next = d;
d.next = e;

/* Function that prints the contents of a linked list */
function printList(node) {
  let current = node;
  
  while (current) {
    console.log(current.value);
    current = current.next;
  }
}

console.log(reverseLinkedList(a));  // should print 'e'
printList(e);   // should print 'e', 'd', 'c', 'b', 'a'