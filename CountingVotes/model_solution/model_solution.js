/*
  O(n) time complexity and O(n) space complexity
*/

function countVotes(arr) {
  const counts = {};
  let maxVotes = 0;
  let winner = '';
  // Iterate over entire array
  arr.forEach(vote => {
    // If name doesnt exist in counts yet, add it with a value of 0
    if (!counts[vote]) counts[vote] = 0;

    // Increment the count of the name
    counts[vote]++;

    // Check to see if current name has more votes then the current max
    if (counts[vote] > maxVotes) {
      // Sets the max votes to the current names votes if larger
      maxVotes = counts[vote];

      // Since this name has more votes, its currently the winner
      winner = vote;

      // Checks to see if current name is tied to the winner
    } else if (counts[vote] === maxVotes) {
      // if tied, sets the winner to the name that is greater (last alphabetically)
      if (vote > winner) winner = vote;
    }
  });
  return winner;
}

console.log(
  countVotes([
    'veronica',
    'mary',
    'alex',
    'james',
    'mary',
    'michael',
    'alex',
    'michael',
  ])
); // should print 'michael'

console.log(
  countVotes([
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
); // should print 'johnny'
