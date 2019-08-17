# Our function traverses the array of prices in a greedy
# fashion, keeping track of both the max profit we've seen
# up to that point as well as the min price we've seen so 
# far. On the next iteration, upate our variables if we find
# find a higher max profit and/or a new min price.
#
# In the case that we receive an array of all descending prices,
# our function will return the least negative value, though this
# is simply a design choice. The interviewee could choose to
# return 0 instead if the function would return a negative value.

def find_max_profit(prices):
    minPrice = prices[0]
    maxProfit = prices[1] - minPrice

    for currentPrice in prices[1:]:
        maxProfit = max(currentPrice - minPrice, maxProfit)
        minPrice = min(currentPrice, minPrice)

    return maxProfit

# Some console.log tests
print(find_max_profit([10, 7, 5, 8, 11, 9]));       # should print 6
print(find_max_profit([1050, 270, 1540, 3800, 2]))  # should print 3530
print(find_max_profit([100, 90, 80, 50, 20, 10]));  # should print -10
print(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]));   # should print 94