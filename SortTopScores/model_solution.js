/* 
  Since we have a highest possible score, we can use 
  a strategy known as a counting sort into to achieve
  a runtime faster than O(n log n).
 */

function sortTopScores(scores, highestPossibleScore) {
  // initialize an array with a length of highestScore
  // then fill it with 0s
  const scoreCounts = Array(highestPossibleScore).fill(0);
  
  // increment the value at the index of `score` 
  // thus we get the count of how many times each score 
  // appears in our `scores` array
  scores.forEach(score => {
    scoreCounts[score]++;
  });

  const sortedScores = [];

  // iterate through our counts array
  // for each count, we add the index of that array slot 
  // that number of times to our array of sorted values
  for (let score = highestPossibleScore; score >= 0; score--) {
    const count = scoreCounts[score];
    // even though we have nested loops here,
    // think about what the time complexity is in terms of 
    // the total number of input elements
    for (let i = 0; i < count; i++) {
      sortedScores.push(score);
    }
  }

  return sortedScores;
}
