# Rock Paper Scissors

What are all the different outcomes to a game of rock, paper, scissors, depending on the numbers of players participating?

Write a function called `rockPaperScissors` that will take as input an integer, `n`, representing the number of players. Your function should output all of the possible combinations of the three plays 'rock', 'paper', or 'scissors' up to the given integer `n`. 

For example, for `n = 2`, your function should output: 
```
[[rock, rock], [rock, paper], [rock, scissors],
 [paper, rock], [paper, paper], [paper, scissors], [scissors, rock],
 [scissors, paper], [scissors, scissors]]
```

So your output should be an array of arrays, where the length of each inner array is `n`. You are ***not*** simulating a game / determining the winner of a game of rock, paper, scissors.
