# For this problem, it's important to think about which 
# data structures to use in order to achieve the functionality
# we're looking for. Think about _why_ these particular data
# structures were used in the solution code. Could we have used
# alternative ones? What would be the resulting tradeoffs?

def balancedBrackets(str):
    line = list(str)  # Convert to array of characters

    # we use a stack to keep track of the opening brackets
    stack = []

    # we use a dict to store the possible openers with
    # their corresponding closers
    openers = {
        '(': ')', 
        '{': '}', 
        '[': ']',
    }

    closers = {
        ')': True, 
        '}': True, 
        ']': True
    }

    for c in line:
        # if we see an opener, push it onto our stack
        if c in openers:
            stack.append(c)
        elif c in closers:
            # if the closer doesn't correspond to the most
            # recently seen unclosed opener, return false
            if (openers[stack.pop()] != c):
                return False

    return len(stack) == 0

# Some console.log tests
print(balancedBrackets('{}[]()'))        # should print True
print(balancedBrackets('{(([]))}'))      # should print True
print(balancedBrackets('{ [ ] ( ) }'))   # should print True
print(balancedBrackets('{ [ ( ] ) }'))   # should print False
print(balancedBrackets('('))             # should print False
print(balancedBrackets('{[}'))           # should print False