# Check if a Linked List is a Palindrome

Suppose we have a singly-linked list (so you can only traverse the list in one direction) class where each list node contains a single character or integer. Implement a function to check if the elements in the linked list form a palindrome.

For example, given the linked list below:
```js
class ListNode {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const a = new ListNode(1);
const b = new ListNode(2);
const c = new ListNode(3);
const d = new ListNode(2);
const e = new ListNode(1);

isLinkedListPalindrome(a);   // should return true
isLinkedListPalindrome(b);   // should return false since now the 'a' node is not included in the linked list
```

Analyze the time and space complexity of your solution.