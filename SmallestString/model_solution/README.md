# Smallest String Walkthrough

## Understanding the Problem

This problem seems to be a variant of the problem of comparing strings that only
contain alphabetic letters. In fact, most languages will already have this
functionality provided out of the box. As a first pass, we could simply
piggyback off of this capability with something like:

```python
def smallest_string(str1, str2):
    # just compare str1 and str2, returning the smallest string
    return str1 if str1 < str2 else str2
```

Let's test this first pass to see if it returns the expected output. When we run
this with the test values, we get the following:

```
smallest_string("a", "b")    # returns a
smallest_string("a1", "a2")  # returns a1
smallest_string("a10", "a2") # returns a10
```

So it looks like our first pass implementation works for the first two inputs,
but it doesn't work for the last example, where the problem statement states
that it should be returning "a2", not "a10" since we are to treat contiguous
numbers as single values. In other words, our function should be treating the
"10" in "a10" as a single number and comparing that against "2". However, with
our current implementation, the "10" is not being treated as a single value and
instead the code is simply comparing "1" and "2", and thus returning "a10" since
"1" comes before "2". 

This seems to be the main hurdle we'll have to overcome when solving this
problem. One question that comes up then is, can we alter our current first-pass
implementation to handle this separate case, or would we need to start over from
scratch? 

If we opt to keep the current logic, then we'd have to add some special handling
to check if we see any consecutive values in either string. If we ascertain that
neither value has consecutive numeric values, then we can probably opt to
fallback on the current logic. Otherwise, we'd have to handle that specific
case. How might we do that?

## Coming Up With A Strategy

While iterating along a string, if we see a number, we'll want to figure out how
many consecutive numbers it contains by iterating over it until we reach the end
of it, so that we know its actual value. Then, if there is a number at the same
index of the other string, we'll have to compare both numbers in their entirety
and return whichever string contains the smaller number. 

In pseudocode, that may look something like:

```
def shortest_string(str1, str2):
    iterate along str1 to see if it contains any consecutive numbers
        if it does, keep iterating along till we reach the end of the number
            store the value of the number and its index 
    do the same thing with str2
    if there are no consecutive numbers in either string
        fall back to our first-pass logic and return the smaller string 
    otherwise, check that the consecutive numbers reside at the same index
        if they don't, i.e. one string contains a number at this index
        and the other string contains a letter, return the other string
```

This doesn't seem very good; it seems like a rather convoluted way of solving
the problem, in large part due to the fact that we're trying to preserve the
first-pass logic that we had. Perhaps it is worth considering removing the
first-pass logic and starting again from the groud up.

We could opt to keep two pointers, one for each string, and then have them
iterate over both strings at the same rate, checking each character one by one.
The nice thing about this is that as soon as we see the two pointers pointing to
different characters, then we can simply return the string whose character comes
earlier. In other words, we'll only traverse the length of the shorter string in
the worst case, since we can return from the function as soon as we notice there
is a character mismatch between both strings. 

In code, this might look like this:

```
def shortest_string(str1, str2):
    initialize variables that start off pointing at the
    starting indices of each string 
    while neither pointer has reached the end of its respective string 
        check if both characters are letters
            if both letters are the same
                advance both indices 
            otherwise, the letters are different
                return the string whose letter is smaller 
        otherwise, at least one of the characters is a number 
            check if both characters are numbers
                parse both numbers to figure out their consecutive values 
                return the string with the smaller numeric consecutive value
            otherwise, one is a letter and the other is a number  
                return the string with the number, since numbers < letters
    if we've reached the end, then one string has run out
    in that case, the shorter string is the smaller one
    return the shorter string 
```

This outlined strategy seems less convoluted than the previous one. In the
worst case, it will perform a single pass through both strings, which is as good
as we can hope for. 

## Implementing the Strategy

Turning the above idea into code. Python has functions `isdigit` and `isalpha` 
that figure out whether a character is a letter or a digit. We can leverage these 
in our implementation:

```python
def shortest_string(str1, str2):
    # indices of both strings 
    s1 = 0
    s2 = 0
    # lengths of both strings 
    len1 = len(str1) - 1
    len2 = len(str2) - 1

    while s1 <= len1 and s2 <= len2:
        # check if both characters are letters 
        if str1[s1].isalpha() and str2[s2].isalpha():
            if str1[s1] == str2[s2]:
                s1 += 1
                s2 += 1
            else:
                return str1 if str1[s1] < str2[s2] else str2
        else:
            if str1[s1].isdigit() and str2[s2].isdigit():
                # parse both numbers 
                n1, l1 = parse_number(str1, s1)
                n2, l2 = parse_number(str2, s2)
                # if the numbers are not equal
                if n1 != n2:
                    # return the string with the smaller number value
                    return str1 if n1 < n2 else str2
                else:
                    # otherwise, we'll need to advance the indices by
                    # the lengths of both consecutive numbers 
                    s1 += l1
                    s2 += l2
            else:
                # one letter and one number 
                return str1 if str1[s1] < str2[s2] else str2
    # we've reached the end of one of the strings
    # the smallest string is the shorter one
    return str1 if len1 < len2 else str2

```

This implementation should do the trick, in lieu of some testing. We left some
logic relegated to a helper function that we haven't defined yet. The
`parse_number` function will be handed a string and an index in the string where 
the the number to parse starts. It will return the consecutive numeric value of
the number it is parsing as well the number's length. The length is needed in
the case that both numbers turn out be the same, in which case we'll need to
advance the string index by the length of the number so that we can continue
iterating along the two strings. 

The `parse_number` method could look like this:

```python
def parse_number(string, index):
    number_length = 0
    number_value = ''
    # loop through the string until we reach a character that isn't a number 
    # we'll also need to make sure that the index doesn't run past the string
    while index <= len(string) - 1 and string[index].isdigit():
        number_length += 1
        number_value += string[index] 
        index += 1
    # don't forget to convert the string number to an int type 
    return (int(number_value), number_length)
```

## Evaluating our Implementation

Our implementation traverses along both strings at the same time, but returns as
soon as it finds a mismatched character between the two strings. Thus, its
runtime is proportional to the length of the shorter of the two strings for a
runtime of O(n). 

With regards to space complexity, extra memory is allocated when we run into a
number and then need to parse it to figure out its actual value including all
the following consecutive numbers. So in the worst case, if both strings contain
only numeric characters, then that much additional memory will need to be
allocated accordingly, which comes out to O(n) space complexity. 
