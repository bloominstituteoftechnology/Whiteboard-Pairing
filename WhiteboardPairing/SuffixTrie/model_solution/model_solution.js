class SuffixTrie {
    constructor(string) {
        this.root = {};
        this.endSymbol = "*";
        this.populateTrie(string);
    }

    populateTrie(string) {
        // loop through each string index
        for (let i = 0; i < string.length; i++) {
            // pass the index to a helper function that
            // is responsible for inserting the substring
            // starting at the given index into the trie
            this.insertSubstringAt(i, string);
        }
    }

    insertSubstringAt(index, string) {
        // keep track of the current node we're traversing on
        let node = this.root;
        // iterate through the string starting at `index`
        for (let i = index; i < string.length; i++) {
            // get the current letter
            const letter = string[i];
            // if the letter isn't contained in the subtree
            if (!(letter in node)) {
                // insert an empty node at this letter
                // so future letters can be added here
                node[letter] = {};
            }
            // set this new node as the current `node` so
            // we can continue traversing down it
            node = node[letter];
        }
        // at this point we've iterated through the entire string
        // and inserted every substring of the input string
        // all that's left is to add the end symbol to the end
        node[this.endSymbol] = true;
    }

    contains(string) {
        // keep track of the current node we're traversing on
        let node = this.root;
        // iterate through the string starting at `index`
        for (let i = 0; i < string.length; i++) {
            // get the current letter
            const letter = string[i];
            // if the letter isn't contained in the subtree
            if (!(letter in node)) {
                // we can stop traversing since we know
                // this string can't be in the trie
                return false;
            }
            // set this new node as the current `node` so
            // we can continue traversing down it
            node = node[letter];
        }
        // at this point we've iterated through the entire string
        // and seen that every letter of the string is in the trie
        // all that's left is to check that the end symbol is at the end
        return this.endSymbol in node;
    }
}