"""
It is recommended that you draw out your algorithm.
It will make a lot more sense that way.
"""

# s is an input Stack
def sort_stack(s):
  # output stack that will hold the sorted elements
  output = Stack()
  # keep sorting until the input Stack is completely empty
  while not s.is_empty():
    temp = s.pop()
    # while the output stack still has elements and its
    # top-most element is larger than the value of temp
    while not output.is_empty() and output.peek() > temp:
      # pop off our output stack back into the input stack
      s.push(output.pop())
    # push temp onto the output stack now that it's in the ordered spot
    output.push(temp)
  return output


class Stack:
  def __init__(self):
    self.storage = []

  def push(self, item):
    self.storage.append(item)

  def pop(self):
    return self.storage.pop()

  def peek(self):
    return self.storage[len(self.storage) - 1]

  def is_empty(self):
    return len(self.storage) == 0

  def print_contents(self):
    for x in self.storage:
      print(x)

  
# Some print tests
s = Stack()
s.push(10)
s.push(4)

sorted_stack = sort_stack(s)
sorted_stack.print_contents()  # should print 4, 10

# print a newline
print()

s.push(8)
s.push(5)
s.push(1)
s.push(6)
s.push(19)
s.push(4)

sorted_stack = sort_stack(s)
sorted_stack.print_contents()  # should print 1, 4, 5, 6, 8, 19