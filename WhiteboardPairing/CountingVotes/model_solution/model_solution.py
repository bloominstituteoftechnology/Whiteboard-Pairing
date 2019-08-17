# O(n) time complexity and O(n) space complexity

def count_votes(arr):
    counts = {}
    max_votes = 0
    winner = ''

    # Iterate over entire array
    for vote in arr:
        # If name doesnt exist in counts yet, add it with a value of 0
        if vote not in counts:
            counts[vote] = 0

        # Increment the count of the name
        counts[vote] += 1

        # Check to see if current name has more votes then the current max
        if counts[vote] > max_votes:
            # Sets the max votes to the current names votes if larger
            max_votes = counts[vote]

            # Since this name has more votes, its currently the winner
            winner = vote

        # Checks to see if current name is tied to the winner
        elif counts[vote] == max_votes:
            # if tied, sets the winner to the name that is greater (last alphabetically)
            if vote > winner:
                winner = vote

    return winner

print(
    count_votes([
        'veronica',
        'mary',
        'alex',
        'james',
        'mary',
        'michael',
        'alex',
        'michael',
    ])
) # should print 'michael'

print(
    count_votes([
        'john',
        'johnny',
        'jackie',
        'johnny',
        'john',
        'jackie',
        'jamie',
        'jamie',
        'john',
        'johnny',
        'jamie',
        'johnny',
        'john',
    ])
)  # should print 'johnny'
