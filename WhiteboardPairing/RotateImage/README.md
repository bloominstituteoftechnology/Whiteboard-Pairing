# Rotate Image

Given an image represented by an `NxN` matrix, where each pixel in the image is an integer from 0 to 9, write a function `rotateImage` that rotates the image by 90 degrees in the counter-clockwise direction. 

For example:
```js
rotateImage([
             [1, 2],
             [3, 4]
           ]);
```
should return 
```
[ 
  [2, 4],
  [1, 3]
]
```
A larger example:
```
rotateImage([
  [1, 1, 5, 9, 9],
  [2, 2, 6, 0, 0],
  [3, 3, 7, 1, 1],
  [4, 4, 8, 2, 2],
  [5, 5, 9, 3, 3]
]);
```
should return
```
[ 
  [ 9, 0, 1, 2, 3 ],
  [ 9, 0, 1, 2, 3 ],
  [ 5, 6, 7, 8, 9 ],
  [ 1, 2, 3, 4, 5 ],
  [ 1, 2, 3, 4, 5 ]
]
```

Analyze the time and space complexity of your solution.

Bonus: Can you do this in-place?