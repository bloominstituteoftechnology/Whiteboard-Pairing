# Time Planner Walkthrough

## Understanding the Problem

This problem gives as input two (sorted) lists of tuples that represent time 
slots of availability for two people who want to find a common time slot of the 
given duration. Let's start off by walking through some examples. 

If we're given the following input:

```
a_slots = [(10, 50), (60, 120)]
b_slots = [(0, 15), (60, 70)]
duration = 8
```

We want to find the earliest time slot where both parties are available for the
given duration. If we just want to time slots when both parties are free for any
length of time, these would be `(10, 15)` and `(60, 70)`. Ok, great. From these,
do any of the satisfy the duration constraint? The `(10, 15)` slot doesn't, that
only lasts for 5 minutes. The `(60, 70)` slot, however, lasts for 10 minutes.
Thus we can fit the 8 minute duration within the 10 minutes of availability, so
our function should return `(60, 68)`. 

What about for the following input:

```
a_slots = [(10, 50), (60, 120)]
b_slots = [(0, 15), (60, 70)]
duration = 12
```

In this case, the common time slots are `(10, 15)` and `(60, 70)`. However, for
a duration of 12 minutes, neither of these common slots are long enough; we only
have 5 minutes of availability with the first slot, and 10 minutes of
availability with the second slot. Therefore, there are no slots that satisfy
the given duration constraint, so our function returns an empty time slot. 

When eyeballing the lists of time slots, how did we actually pick out the common
time slots? Well, if the start time of one slot falls between the starting and
ending time of another time slot, then there's some overlap. How long is that
overlap? The first ending time of either slot determines the ending time of the
common slot. 

Let's break that down a bit further. Given two time slots `(10, 60)` and `(30,
75)`, we see that the start time of 30 falls within 10 and 60, so there's a
commonality there. This commonality ends when we encounter the soonest ending
time, which is 60. So the common time slot here is `(30, 60)`. 

With an example like `(4, 15)` and `(16, 27)`, there's no commonality because
neither starting time falls within the range of the other time slot. We could
also have `(10, 55)` and `(14, 50)`, where the second time slot falls completely
within the bounds of the first time slot such that the common time slot is just
the second time slot, `(14, 50)`. 

Now that we understand logically how to pick out common time slots, let's see if
we can come up with a strategy for solving this problem. 

## Coming Up With A Strategy

How do we check for common slots given two time slots in code? Of the two
starting times, we want to figure out the larger of the two times to figure out
the starting time of the common time slot. Similarly, to figure out the ending
time of the common time slot, we want to figure out the smaller of the two
ending times. We can use `max` and `min` functions to do this. 

We can use a nested loop to check every time slot from one list of time slots
against every time slot from the other list, seaching for commonalities along
the way. This would yield an O(n * m) runtime where n and m are the lengths of
both lists respectively, and might look like this:

```
def time_planner(a_slots, b_slots, duration):
    loop through all time slots in a_slots
        loop through all time slots in b_slots 
            find starting time by checking for max of both starting times
            find ending time by checking for min of both ending times
            check if ending time - starting time >= duration 
                if so, return (starting time, starting time + duration)
    otherwise, there are no common time slots
```

The resulting code could look like this:

```python  
def time_planner(a_slots, b_slots, duration):
    for a_slot in a_slots:
        for b_slot in b_slots:
            start = max(a_slot[0], b_slot[0])
            end = min(a_slot[1], b_slot[1])
            if end - start >= duration:
                return (start, start + duration)
    return ()
```

Of course, the next question now becomes, can we achieve a better runtime than
O(n * m)? Do we need to loop through every single permutation of time slots
between the two lists?

Whenever we're given sorted input, chances are we can make use of that fact in
some way. Since the time slots in both lists are sorted by starting time,
perhaps we don't need to check every time slot from the first list against all
the time slots in the second list. There's no need to check any time slots where
the starting time has already surpassed the ending time. 

To facilitate this idea, we could use two indices to keep track of our progress 
as we're iterating through both lists in a single loop. We'll still perform the
same logic of determining the starting and ending time of the common time slot
by determining the max starting time and min ending time of the two time slots.
Then, we'll decide which index to update by checking which time slot has the
smaller ending time.

## Implementing and Evaluating Our Strategy

In pseudocode, that could look like this:

```
def time_planner(a_slots, b_slots, duration):
    initialize two index variables, a and b, to 0
    loop so long as a and b are within bounds of their respective lists
        find starting time by checking for max of both starting times
        find ending time by checking for min of both ending times
        check if ending time - starting time >= duration 
            if so, return (starting time, starting time + duration)
        check if the ending time from the a list < ending time from the b list
            if it is, increment the a index
        otherwise
            increment the b index 
    if we haven't found a common time slot
        return empty list
```

The resulting code could look like this:

```python
def time_planner(a_slots, b_slots, duration):
    a = 0
    b = 0

    while a < len(a_slots) and b < len(b_slots):
        start = max(a_slots[a][0], b_slots[b][0])
        end = min(a_slots[a][1], b_slots[b][1])

        if end - start >= duration:
            return (start, start + duration)            

        if a_slots[a][1] < b_slots[b][1]:
            a += 1
        else:
            b += 1

    return ()
```

With this implementation, we perform a single pass through both lists, stopping
iteration whenever we reach the end of the shorted input list. Thus, this
exhibits a runtime of O(n). Space complexity is O(1) since we only ever
initialize a constant amount of extra memory. 

