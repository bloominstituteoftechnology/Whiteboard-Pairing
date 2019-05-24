class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.end_symbol = "*"
        self.populate_trie(string)

    def populate_trie(self, string):
        # loop through each string index
        for i, _ in enumerate(string):
            # pass the index to a helper function that 
            # is responsible for inserting the
            # substring starting at the given index
            # into the trie
            self.insert_substring_at(i, string)

    def insert_substring_at(self, index, string):
        # keep track of the current node we're traversing on
    	node = self.root
	# iterate through the string starting at `index`
    	for letter in string[index:]:
	    # if the letter isn't contained in the subtree
    	    if letter not in node:
		# insert an empty node at this letter
                # so future letters can be added here
    		node[letter] = {}
	    # set this node as the current `node` so 
            # we can continue traversing down it
    	    node = node[letter]
	# we've iterated through the entire string
        # and inserted every substring of the input string
	# all that's left is to add the `end_symbol` to the end
    	node[self.end_symbol] = True

    def contains (self, string):
        # keep track of the current node we're traversing on
        node = self.root
        # iterate through the string
        for letter in string:
            # if the letter isn't contained in the subtree
            if letter not in node:
                # we can stop looking
                return False
            # set this node as the current `node` so we
            # can continue traversing down it
            node = node[letter]
        # we've iterated through the entire string
        # all the letters in the target string were in the trie
        # all that's left is to check for the end symbol at the end
        return self.end_symbol in node
