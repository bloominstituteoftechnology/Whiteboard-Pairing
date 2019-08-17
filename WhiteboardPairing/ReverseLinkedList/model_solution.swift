class ListNode<T>: CustomStringConvertible {

  var value: T
  var next: ListNode?
  
  init(value: T, next: ListNode<T>? = nil) {
    self.value = value
    self.next = next
  }
  
  var array: [T] {
    var result = [T]()
    var current: ListNode<T>? = self
    while current != nil {
      result.append(current!.value)      
      current = current?.next
    }
    return result
  }
  
  var description: String {
    return array.description
  }
}

func reverse<T>(linkedList: ListNode<T>) -> ListNode<T> {
  var current: ListNode<T>? = linkedList
  var nextNode: ListNode<T>?
  var prevNode: ListNode<T>?
  
  while current != nil {
    // store a reference to the next list node
    // before we overwrite current.next
    nextNode = current?.next
    
    // reverse the 'next' pointer
    current?.next = prevNode
    
    // step forward to the next list node
    prevNode = current
    current = nextNode
  }
  
  return prevNode!
}

let e = ListNode(value: "e")
let d = ListNode(value: "d", next: e)
let c = ListNode(value: "c", next: d)
let b = ListNode(value: "b", next: c)
let a = ListNode(value: "a", next: b)

print(a)
print(reverse(linkedList: a))