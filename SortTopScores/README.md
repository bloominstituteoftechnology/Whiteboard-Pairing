# Sort Top Scores

You wrote a popular game with a highest possible score of 1000. Currently, you're using a sorting method with a runtime of O(n log n). However, your sorting algorithm is slowing down the overall performance of your game, and players are complaining. 

Given that your game has a highest possible score, can we take advantage of this fact to write a sorting algorithm that achieves better than O(n log n)?

Your sorting algorithm should return an array of all the sorted scores with the highest scores at the beginning of the array, with the rest of the elements in descending order. Make your general-purpose such that it can accept a `highestPossibleScore` as a parameter, in case we need to raise the highest possible score of our game. 

Analyze the time and space complexity of your solution.