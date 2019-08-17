 # Suffix Trie

A suffix trie is a tree data structure that stores suffixes of strings. Visually, you could draw a suffix trie like so:

[Suffix trie drawing here]

In code, we can represent such a data structure using nested hash tables. For example, for the string "babc", it would look like this:
```
{
    "c": {"*": True},
    "b": {
        "c": {"*", True},
        "a": {
            "b": {
                "c": {"*", True}
            }
        }
    },
    "a": {
        "b": {
            "c": {"*": True}
        }
    }
}
```

Write a class for a such a suffix trie data structure. This class should have a root property representing the root node of the trie. It should support creation from an initial string passed to the constructor as well as searching of strings.

The creation method will be called when the class is instantiated and should populate the root node with a subtries containing all of the suffixes of the given string. Note that every string added to the trie should end with the "endSymbol" character "*".

```
trie = SuffixTrie("pogo")
print(trie.root)  # should print the following
{
    "p": {
        "o": {
            "g": {
                "o": {'*': True}
            }
        }
    }, 
    "o": {
        "g": {
            "o": {'*': True}
        }, 
        "*": True}, 
    "g": {
        "o": {'*': True}
    }
}

print(trie.contains("ogo"))  # should print True
```