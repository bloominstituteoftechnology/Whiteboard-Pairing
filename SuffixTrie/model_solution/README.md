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
{
    "p": {
          "o": {
                "g": {
                      "o": {"*": True}
                }
          }
    }, 
    "o": {"*": True}, <--- is this what we're supposed to get?
    "g": {
          "o": {"*": True}
    }
}
```

Wait, that's not right.. The root level "o" entry should have a nested
"g" and then another "o" nested inside the "g" node, since "ogo" is a
suffix of "pogo". 

So it looks lik we have a problem with our implementation. The problem
is that our current implementation isn't checking for if the letter
we're trying to insert into a node in the trie already exists. So what's
happening here is that we _did_ insert "ogo" at the root level of the
trie, and then we continued on, inserting "go", and finally the last
"o". But, since our code isn't checking if letters already exist in any
given node, the act of inserting the last "o" overwrites the previous
"ogo" entry. 

We can remedy this pretty easily by changing our `populate_trie` to the
following:

```python
def populate_trie(self, string):
    node = self.root
    index = 0
    while index < len(string):
        for letter in string[index:]:
            # we'll add a check here to see if the letter already
            # exists in the current node; if it does, then we 
            # don't want to overwrite it 
            if letter in node:
                # only add a new hash table in the case that this
                # node doesn't contain the given letter 
                node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = True
        index += 1
```

This change will result in the following:

```
{
    "p": {
          "o": {
                "g": {
                      "o": {"*": True}
                }
          }
    }, 
    "o": {  <--- this is what we expected to see 
          "g": {
                "o": {"*": True}
          }
    },
    "g": {
          "o": {"*": True}
    }
}
```

Now our implementation is producing the expected result! 

### Step 5: Implementing `contains`

Phew! That was a lot of work to get `populate_trie` working! The good
news is that we're more than halfway through at this point. That's
because the `contains` method looks very similar to the `populate_trie`
method. 

Let's step back and think about the logic of how we'll search through 
the trie for some target string. Since our trie stores individual
letters, it makes sense then to traverse our target string, checking
along the way if the trie contains the letter in the node we're
currently traversing on. 

Our `populate_trie` method already performs traversal through the trie,
so that's all logic we can re-use. All that's left then is to check to
see if at each traversal, the letter in the trie matches the letter in
the target string in the order that we're expecting. 

Hashing this idea out into code, we might get something like this:

```python
def contains(self, string):
    # we'll also keep track of the current node here so
    # we know where in the trie we are as we're traversing
    node = self.root
    # iterate along the input string we're searching for
    # in our trie
    for letter in string:
        # check if the current letter is not in the current node
        if letter not in node:
             # if it isn't, then we can stop here, since we know
             # that the string can't be in the trie
             return False
        # otherwise, continue to traverse down the trie by 
        # setting our `node` variable to be the node containing
        # the current letter 
        node = node[letter]
    # at this point we've checked that every letter in the input 
    # string is contained in our trie in the correct order, so
    # we've found the string; let's finally check to make sure 
    # the word ends with our ending symbol
    return self.end_symbol in node
```

The last line in the above implementation is a bit a formality. After
all, if a word in our trie _doesn't_ end with the ending symbol, well,
that was because we forgot to add it ourselves. 

As we can see though, our `contains` implementation looks a heck of a
lot like our `populate_trie` implementation. 

### Step 6: Cleaning up our code 

There's a bit we can do here to clean up our implementation to make it
more readable and more modular. One thing would be to split off some of
the logic of our `populate_trie` function into a helper method. The
helper method will be responsible for inserting a single substring of
a given string into our trie, with the substring being delineated by the
index of where the substring starts in the original string. So we might
end up with something like this:

```python
def insert_substring_at(self, index, string):
    # we'll move all of the traversal logic from our 
    # `populate_trie` method into this helper 
    node = self.root
    for letter in string[index:]:
        if letter not in node:
            node[letter] = {}
        node = node[letter]
    node[self.end_symbo] = True

def populate_trie(self, string):
    # our `populate_trie` method will then just be 
    # responsible for looping through the input string
    # and passing in the index of each substring as it
    # does so
    for i in range(len(string)):
        self.insert_substring_at(i, string)
```

This makes our implementation a bit cleaner, since now we have a
separate functions, one for handling insertion of individual substrings,
and the other responsible for iterating along the string and producing
each substring to insert. 

### Step 7: Analyzing time and space complexity

To figure out the time complexity goes when it comes to creation, a helpful hint
for figuring this out is to look at our `populate_trie` method before we
split off the traversal logic into a helper function. 

```python
def populate_trie(self, string):
    node = self.root
    index = 0
    while index < len(string):
        for letter in string[index:]:
            node[letter] = {}
            node = node[letter]
        node[self.end_symbol] = True
        index += 1
```

Takinga a look at this code, we see that we have a while loop that
iterates along the entire length of the input string, followed by a
nested for loop along the entire length of the substring. In the worst
case, these nested loops will yield an O(m^2) runtime, where m is the
length of the input string. 

As far as space complexity goes, we just determined that creation takes
O(m^2) time. Then, since we're sticking all of those m^2 letters in our
trie, it turns out that the space complexity of our trie data structure
is proportional to our time complexity, so space complexity is also
O(m^2) in this case. 

What about searching for some given string in our trie? Well, in that
case, we only ever have to perform the same number of checks as there
are letters in our target string. The beauty of a trie data structure is
that this fact holds true _regardless_ of how many strings are being
stored in our trie. We could have a whole bunch of strings in a single
trie and runtime for searching for any arbitrary string in the trie
would always just be proportional to the length of the target string.
Thus, searching through our trie takes O(m) time, where m is the length
of whatever target string we'd like to search for. 

So there you have it. That's a pretty thorough walkthrough of
implementing a suffix trie data structure. Remember, the whole point of
a trie data structure is to provide fast lookup of strings (think about
what the runtime would be if we instead just had a bunch of strings in
an array; what would the runtime be to search for a single string in
that case?). However, the tradeoff we incur for this fast lookup is slow
insertion as well as taking up a relatively large amount of memory. 

