class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    # If we reach the capacity of the buffer
    # set the current pointer back to the beginning
    if self.current == self.capacity:
      self.current = 0

  def allValues(self):
    return self.storage


# Some console.log tests 
buffer = RingBuffer(5)

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.allValues())  # should print ['a', 'b', 'c', 'd', 'None']

buffer.append('e');
print(buffer.allValues())  # should print ['a', 'b', 'c', 'd', 'e']

buffer.append('f');
print(buffer.allValues())  # should print ['f', 'b', 'c', 'd', 'e']

buffer.append('g');
buffer.append('h');
buffer.append('i');
print(buffer.allValues())  # should print ['f', 'g', 'h', 'i', 'e']
