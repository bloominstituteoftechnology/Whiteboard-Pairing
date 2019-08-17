# O(2n) time complexity with O(2n) space complexity

def reconstructTrip(tickets):
  # use an object to associate sources
  # and destinations
  hash = {};
  route = [None]*(len(tickets) - 1)

  for ticket in tickets:
    # check for the start destination of our trip
    if ticket[0] == None:
      # add it to our `route` array as the first element
      route[0] = ticket[1]
    
    # hash each ticket with the source as key
    # and destination as value
    hash[ticket[0]] = ticket[1]

  # loop through our object, grabbing the source's
  # associated destination and adding it to our route
  for i in range( 1, len(tickets)-1):
    route[i] = hash[route[i-1]]

  return route
  

# Some tests
shorterSet = [
  [None, 'PDX'],
  ['PDX', 'DCA'],
  ['DCA', None],
]

longerSet = [
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
]

print(reconstructTrip(shorterSet)); # should print [ 'PDX', 'DCA' ]
print(reconstructTrip(longerSet));  # should print [ 'LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD' ]
