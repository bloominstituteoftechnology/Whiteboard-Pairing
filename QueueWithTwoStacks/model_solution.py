class Queue:
  def __init__(self):
    # Stack to hold elements that get added
    self.inStack = []
    # Stack to hold elements that are getting removed
    self.outStack = []
  

  def enqueue(self, item):
    self.inStack.insert(0, item)
  

  def dequeue(self):
    # if the outStack is empty
    # we need to populate it with inStack elements
    if len(self.outStack) == 0:
      # empty out the inStack into the outStack
      while len(self.inStack) > 0:
        self.outStack.insert(0, self.inStack.pop(0))
      
    return self.outStack.pop(0)


  def peek(self):
    # same logic as `dequeue`
    if len(self.inStack) == 0:
        return None
    else:
      while len(self.inStack) > 0:
        self.outStack.insert(0, self.inStack.pop(0))
    
    return self.outStack[0]
    

# Some console.log tests 
q = Queue()
print(q.peek())   # should print None

q.enqueue(10)
print(q.peek())   # should print 10

q.enqueue(9)
q.enqueue(8)

print(q.dequeue())   # should print 10
print(q.dequeue())   # should print 9
print(q.dequeue())   # should print 8
