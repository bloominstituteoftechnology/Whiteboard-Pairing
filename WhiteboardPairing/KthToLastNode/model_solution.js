/* 
  This algorithm maintains a k-wide 'window' with two pointers 
  and makes one walk down the linked list. When the pointer in 
  front reaches the end of the list, the second pointer will be 
  at the node we're looking for.

  Another approach could be walking down the list to count the
  length of the list, subtract k from the total length, and
  then walking to that node.

  Think about some of the tradeoffs between these two approaches.
*/

function kthToLastNode(k, head) {
  if (k < 1) {
    throw new Error('Impossible to find less than first to last node: ' + k);
  }

  let leftNode = head;
  let rightNode = head;

  // move rightNode to the kth node
  for (var i = 0; i < k - 1; i++) {

    // but along the way, if a rightNode doesn't have a next,
    // then k is greater than the length of the list and there
    // can't be a kth-to-last node! we'll raise an error
    if (!rightNode.next) {
      throw new Error('k is larger than the length of the linked list: ', k);
    }

    rightNode = rightNode.next;
  }

  // starting with leftNode on the head,
  // move leftNode and rightNode down the list,
  // maintaining a distance of k between them,
  // until rightNode hits the end of the list
  while (rightNode.next) {
    leftNode = leftNode.next;
    rightNode = rightNode.next;
  }

  // since leftNode is k nodes behind rightNode,
  // leftNode is now the kth to last node!
  return leftNode.value;
}

class ListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

let a = new ListNode("Australian Sheperd");
let b = new ListNode("Beagle");
let c = new ListNode("Cairne Terrier");
let d = new ListNode("Dobermann");
let e = new ListNode("English Mastiff");

a.next = b;
b.next = c;
c.next = d;
d.next = e;

/* Some console.log tests */
console.log(kthToLastNode(2, a));   // should print 'Dobermann'
console.log(kthToLastNode(5, a));   // should print 'Australian Sheperd'
console.log(kthToLastNode(3, c));   // should print 'Cairne Terrier'