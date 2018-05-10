/*
  O(2n) time complexity and O(n) space complexity
*/

function countVotes(votes) {
  // use a hash to store names and their number of votes
  const hash = {};

  // insert by name and number of occurrences into our map
  votes.forEach(vote => {
    // if name doesn't exist in hash, initialize it
    if (!hash[vote]) {
      hash[vote] = 1;
    }

    // if it does exist, increment the count
    hash[vote]++;
  });

  let winner;
  let winnerCount = 0;

  // loop through all our hash entries
  Object.entries(hash).forEach(([name, count]) => {
    // if we've found a higher number of votes
    // update `winner` to be that person
    // don't forget to update `winnerCount`
    if (count > winnerCount) {
      winnerCount = count;
      winner = name;
    }
    // if there's a tie, pick the person whose
    // names shows up later in the alphabet
    else if (count === winnerCount) {
      winner = name > winner ? name : winner;
    }
  });

  return winner;
}

console.log(countVotes(
  ['veronica', 'mary', 'alex', 'james', 'mary', 'michael', 'alex', 'michael']
));  // should print 'michael'

console.log(countVotes(
  ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john","johnny", "jamie", "johnny", "john"]
));   // should print 'john'