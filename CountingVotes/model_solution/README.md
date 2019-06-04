# Counting Votes Walkthrough

## Understanding the Problem

The problem is asking us to figure out the winner of an election given a list of
names where each name constitutes a vote for that candidate. What do we need to
keep track of in order to handle that?

Well, we'll need to know how many votes each candidate received. Once we know
that, we can figure out, based off of who has the most votes, who won the
election. We'll also need to handle the case when there is a tie. The problem
states that in such a scenario, of the candidates who have the most votes, the
candidate whose name comes last alphabetically wins the election. 

Let's go through a few simple examples. If we receive the following list of
names `['jack', 'jill', 'jill']`, then Jill will be declared the election
winner. If we have `['jack', 'jill', 'jill', 'jack']`, then Jill should still
win since her name comes after Jack's alphabetically. 

## Coming up with a Strategy

Our first step is figuring out how many votes each candidate receives from the
list of names. One of the best ways achieve this step is to use a hash table (an
Object) to store names as keys and counts as values. So the idea becomes: we'll
iterate over the names in the list, we'll check to see if our hash table already
contains the given name. If it does, we'll increment its associated count. If it
doesn't, then we'll add it to the hash table with a count of 1, since that will
have been the first time we've seen that particular name. 

```
def count_votes(votes):
    initialize hash table to store counts of each name
    counts = {}

    loop through each name in the `votes` list
        if the name is in `counts`
            increment the value associated with the name 
        otherwise, we haven't seen this name before
            add it to `counts` with 1 as its value 
```

At this point, we'll have every each name in the hash table along with the total
number of times we've seen each name. Now we'll need to figure out which name
earned the most votes. 

To do that, we'll need to loop through each key-value pair in `count`; we can
figure out who has the most votes the way we always do: by keeping track of the
highest number we've seen so far and when we see a key-value pair whose value is
greater than the value we've seen so far, we'll update the variable. We'll want
to keep a separate variable for the name of the winner in addition to the number
of votes they had.

That might look like the following:

```
max_votes = 0
winner = ''

loop through the key-value pairs in `counts`
    if value > max_votes value
        max_votes = value
        winner = key
```

By the end of this iteration, `max_votes` will hold the key-value pair with the
highest number of votes, along with the name associated with those votes. So we
can then return that name. 

## Implementing our Strategy

Let's combine these two ideas together in code. With what we have so far, our
solution might look like this:

```python
def count_votes(votes):
    counts = {}

    for name in votes:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    
    max_votes = 0
    winner = ''

    for name, votes in counts:
        if votes > max_votes:
            max_votes = votes
            winner = name

    return winner
```

This implementation figures out the winner when there is a clear winner amongst 
the candidates. As of yet, it doesn't handle ties. How would we handle those?
Well, a tie results when we've found a candidate who has the same number of
votes as the winner. That would seem to imply that we'll want to perform a
separate check to see if the number of votes for the current name we're
iterating on matches the number of votes of the current winner. If so, then
we'll want to set the value of the `winner` variable to be the name that comes
last in the alphabet. Let's add that logic to our implementation:

```python
def count_votes(votes):
    counts = {}

    for name in votes:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1
    
    max_votes = 0
    winner = ''

    for name, votes in counts:
        # check to see if we've found a candidate with the same
        # number of votes as our current winner
        if votes == max_votes:
            # set the value of `winner` to be the name that 
            # comes later in the alphabet 
            winner = name if name > winner else winner
        elif votes > max_votes:
            max_votes = votes
            winner = name

    return winner
```

Cool! This implementation now handles ties correctly. 

## Evaluating and Improving our Strategy

What's the runtime of this implementation? As far as space complexity goes,
we're inserting each unique name into a hash table, so in the worst case, the
hash table will contain as many entries as there are names in the input list.
That introduces a space complexity of O(n). 

As for time complexity, we perform two linear passes through the data, the first
time through the `votes` array, the second time through all of the key-value
pairs in `counts`. So the overall runtime is O(2n), or O(n). 

With that being said, do we need to perform two passes through the data? Could
we combine both linear passes into a single pass? 

We can indeed:

```python
def count_votes(votes):
    counts = {}
    max_votes = 0
    winner = ''

    for name in votes:
        if name in counts:
            counts[name] += 1
        elif name not in counts:
            counts[name] = 1
        elif counts[name] > max_votes:
            max_votes = counts[name]
            winner = name
        elif counts[name] == max_votes:
            winner = name if name > winner else winner

    return winner
```

This implementation achieves the same space complexity and theoretical time
complexity, though in practice it will handle large inputs faster than the
previous solution since it only performs a single pass through the data.
