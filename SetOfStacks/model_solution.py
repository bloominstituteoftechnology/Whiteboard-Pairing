class SetOfStacks:
  def __init__(self, capacity):
    self.capacity = capacity
    self.stacks = [[]]
    # the index of the current stack we're on
    self.stack_index = 0

  # returns the number of stacks
  def __len__(self):
    return self.stack_index + 1

  def push(self, item):
    # check to see if the current stack has room
    if len(self.stacks[self.stack_index]) < self.capacity:
      self.stacks[self.stack_index].append(item)
    else:
      # current stack has reached its capacity
      # add a new stack to the stack of stacks and append to the new stack
      self.stacks.append([])
      self.stack_index += 1
      self.stacks[self.stack_index].append(item)

  def pop(self):
    # check to see if the current stack is empty
    if len(self.stacks[self.stack_index]) == 0:
      self.stack_index -= 1
    return self.stacks[self.stack_index].pop()

  """
  There are a couple of ways this `popAt` function could be implemented.
  We could simply pop from the stack at the given index and call it a day.
  However, this might lead to tricky situations later on if someone
  assumes that all stacks other than the last one operate at full capacity.

  The alternative is to pop from the stack at the given index, and then 
  roll over an item from the next stack, which would get us into a chain
  reaction of having to roll over an item from every stack to the previous
  stack until we reach the last stack. 

  There are signicant time complexity tradeoffs between these two approaches.
  Be sure to discuss these tradeoffs with your interviewee.
  """
  # pop_at implementation with no rolling over of elements
  # we simply pop from the stack at the specified index
  # what is the time complexity of this method?
  def pop_at_no_rollover(self, index):
    return self.stacks[index].pop()

  # a pop_at implementation that exhibits rolling over of elements
  # what is the time complexity of this method?
  def pop_at_with_rollover(self, index):
    return self._shift_stacks(index)

  # recursive helper method to continually shift elements down each stack
  def _shift_stacks(self, index):
    # shift off the first element of the stack at the specified index
    # this is the element we're going to return
    rv = self.stacks[index].pop(0)
    # check to see if the specified stack would be left with no elements
    if len(self.stacks[index] == 0):
      self.stacks.pop(index)
    elif len(self.stacks) > index + 1:
      v = self._shift_stacks(index + 1)
      self.stacks[index].append(v)
    return rv

# Some print tests
stacks = SetOfStacks(3)
stacks.push(6)
stacks.push(8)
stacks.push(3)
print(len(stacks))                   # should print 1

stacks.push(4)
print(len(stacks))                   # should print 2

print(stacks.pop_at_no_rollover(0))  # should print 3

print(stacks.pop())                  # should print 4
print(stacks.pop())                  # should print 8
print(len(stacks))                   # should print 1 