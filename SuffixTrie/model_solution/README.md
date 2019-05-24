# Suffix Trie Walkthrough

## What even is a suffix trie?

Tries are a type of tree data structure that are efficient when it comes
to storing and searching through strings. They achieve this efficiency
by storing either prefixes or suffixes of strings character by
character. A suffix trie then is a trie that stores all the suffixes of
the strings it contains (a prefix trie would thus be a trie that stored
all the prefixes of the strings it contains). 

For example, all the suffixes of the word "cat" would be:
1. "t" -- the last character in the word
2. "at" -- the last two characters in the word
3. "cat" -- the entire word itself; every word is considered a suffix of
   itself by default

So a suffix trie that contained the word "cat" would contain all three
of the listed suffixes. We could visualize such a trie like so:

[Image of suffix trie here]

## Examining the code that's already here

The provided skeleton class has a root, which is an empty hash table, an
ending symbol that we'll use to mark the end of a string, as well as a
`populate_trie` method that it calls with the input string that is
passed to the constructor of the class. The methods that need
implementing are the `populate_trie` method, which will add a given
input string to the trie, as well as a `contains` method, which will
return a boolean indicating whether a given input string exists in the
trie.

## So how do we build this thing?

Let's start by working on the `populate_trie` method before we turn our
attention to the `contains` method. One helpful way to think about
implementing a method like this is to start with a very simple case,
and then work our way up to more general cases, so let's do that. 

### Step 1: Inserting a single letter 

The problem description prescribes using nested hash tables
(objects/dictionaries) in order to represent this trie structure. When
walking through how to build this, it helps to start very simple. What
does a suffix trie that's holding a single letter look like? It would
look like this:

```
{
    "x": {"*": True}
}
```

The keys will be the letters themselves, with their associated value
being another hash table that holds all the children nodes of the 
letter. In this case, a node's children will be all the letters that
come after it in the string. If we just have a solitary letter with no
children, this will be denoted by a hash table whose single key-value
pair is `"*": True`. 

For the single letter case, it would suffice to simply do 

```python
def populate_trie(self, string):
    # in this example, `string` is just a single letter
    self.root[letter] = {"*": True}
```

where `letter` is the letter we're looking to insert. We just need to
add a key value pair to the root node whose key is "c" and whose value
is `{"*": True}`. 

### Step 2: Adding longer strings

Ok, let's extend what we currently have so that we can add full-on
words, not just single letters. If we want to insert "cat", what would
that look like?

Let's start over with an empty trie with nothing in it. Now, to add the
word "cat" to the trie, we'll need to add every letter in the word one
character at a time. That might look something like this:

```python
def populate_trie(self, string):
    # we'll keep track of the current node we at in the trie
    # since we'll be traversing further and further down the 
    # trie with every letter we add
    node = self.root

    for letter in string:
        # add this letter to the current node as a child 
        # by adding the letter as a key with an empty 
        # hash table as its value 
        node[letter] = {}
        # now update the `node` variable since we're still
        # traversing down the trie 
        node = node[letter]
    # now that we're done iterating, we have the entire string
    # in the trie; add the end symbol to indicate this string
    # is complete
    node[self.end_symbol] = True
```

Running this method with the string "cat" will produce the following
structure (if you aren't convinced of this, trace through the code by
drawing out its execution using pencil and paper to convince yourself):

```
{
    "c": {
        "a": {
            "t": {"*": True}
        }
    }
}
```

### Step 3: Handling all suffixes 

That's good progress! But that's not everything yet. Remember, our
suffix trie should contain _every_ suffix of the word, not just the word
by itself.

Ok, well, that should be pretty simple. We can start off by inserting
the whole word like we just did, and then insert the whole word minus
the first letter, and then insert the whole word minus the first two
letters, etc. We'll do this until we get to the last letter of the word. 

To do this, we'll update our `populate_trie` method like so:

```python
def populate_trie(self, string):
    node = self.root
    # we'll want to keep track of the starting index
    # of the string that we're going to insert
    index = 0
    # we'll keep adding substrings of the input string
    # until we've added every single one, that is, 
    # until our index has reached the length of the string
    while index < len(string):
        # iterate through the string starting at `index` 
        # instead of iterating along the whole string 
        for letter in string[index:]:
            node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = True
        # increment the index now that we've added this substring
        index += 1
```

This updated implementation will now yield the following when we run it
with the string "cat":

```
{
    "c": {
        "a": {
            "t": {"*": True}
        }
    },
    "a": {
        "t": {"*": True}
    },
    "t": {"*": True}
}
```

Perfect! That's exactly what we want our suffix trie to look like when
we insert the string "cat". 

### Step 4: Dealing with repeated letters

What happens when we run this method on a word that has some repeating
letters? Let's say a word like "pogo". If you go ahead and test this out
for yourself, you should see that the resulting trie looks like the
following:

```

```
