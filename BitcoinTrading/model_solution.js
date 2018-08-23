/* 
  Our function traverses the array of prices in a greedy
  fashion, keeping track of both the max profit we've seen
  up to that point as well as the min price we've seen so 
  far. On the next iteration, upate our variables if we find
  find a higher max profit and/or a new min price.

  In the case that we receive an array of all descending prices,
  our function will return the least negative value, though this
  is simply a design choice. The interviewee could choose to
  return 0 instead if the function would return a negative value.
*/

function findMaxProfit(prices) {
  let minPrice = prices[0];
  let maxProfit = prices[1] - minPrice;

  for (let i = 1; i < prices.length; i++) {
    const currentPrice = prices[i];

    maxProfit = Math.max(currentPrice - minPrice, maxProfit);
    minPrice = Math.min(currentPrice, minPrice);
  }

  return maxProfit;
}

/* Some console.log tests */
console.log(findMaxProfit([10, 7, 5, 8, 11, 9]));       // should print 6
console.log(findMaxProfit([1050, 270, 1540, 3800, 2]))  // should print 3530
console.log(findMaxProfit([100, 90, 80, 50, 20, 10]));  // should print -10
console.log(findMaxProfit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]));   // should print 94