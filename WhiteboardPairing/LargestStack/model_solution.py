class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        else:
            return None

class MaxStack:
    # We use two Stacks, one to store all the values
    # The other to store just our max values
    def __init__(self):
        self.stack = Stack()
        self.maxValues = Stack()

    def push(self, item):
        self.stack.push(item)
        # If the given item is larger than the
        # latest max value, add it to the stack
        # of max values as the new max
        peekValue = self.maxValues.peek()
        if peekValue is None or item >= peekValue:
            self.maxValues.push(item)

    def pop(self):
        item = self.stack.pop()
        # check to see if the item we popped off
        # is the current max
        # if it is, pop off the max Stack
        # the previous max value in the Stack
        # takes its place
        if item == self.maxValues.peek():
            self.maxValues.pop()

        return item

    def getMax(self):
        return self.maxValues.peek()


maxStack = MaxStack()
print(maxStack.getMax())   # should print None

maxStack.push(1)
print(maxStack.getMax())   # should print 1

maxStack.push(100)
print(maxStack.getMax())   # should print 100

maxStack.pop()
print(maxStack.getMax())   # should print 1

