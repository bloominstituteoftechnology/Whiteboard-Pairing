/* 
  O(2n) time complexity with O(2n) space complexity
*/

function reconstructTrip(tickets) {
  // use an object to associate sources
  // and destinations
  const hash = {};
  const route = Array(tickets.length - 1);

  tickets.forEach(ticket => {
    // check for the start destination of our trip
    if (ticket[0] === null) {
      // add it to our `route` array as the first element
      route[0] = ticket[1];
    }
    // hash each ticket with the source as key
    // and destination as value
    hash[ticket[0]] = ticket[1];
  });

  // loop through our object, grabbing the source's
  // associated destination and adding it to our route
  for (let i = 1; i < tickets.length - 1; i++) {
    route[i] = hash[route[i-1]];
  }

  return route;
}

/* Some console.log test */
const shorterSet = [
  [null, 'PDX'],
  ['PDX', 'DCA'],
  ['DCA', null],
];

const longerSet = [
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [null, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', null],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
];

console.log(reconstructTrip(shorterSet)); // should print [ 'PDX', 'DCA' ]
console.log(reconstructTrip(longerSet));  // should print [ 'LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD' ]