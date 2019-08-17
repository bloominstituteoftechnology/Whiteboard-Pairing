# Find Rotation Point
You went and bought a copy of Webster's English dictionary on April Fool's Day and received the joke edition of the dictionary. You open it up and see that the first entry in the dictionary starts somewhere in the middle. Once the end of the alphabet is reached, it circles around and starts over at the 'A' section and goes all the way through until it reaches the beginning. Otherwise, though, everything else seems to be in order. 

For example, a rotated list of words might look something like this:
```js
const words = [
  'ptolemaic',
  'retrograde',
  'supplant',
  'undulate',
  'xenoepist',
  'asymptote',    // <-- rotation happens here
  'babka',
  'banoffee',
  'engender',
  'karpatka',
  'othellolagkage',
]
```

Write a function `findRotationPoint` that receives an array of words and calculates the index of the point where the rotation occurs. With the above list of words, your function would return 5. 

Analyze the time and space complexity of your solution. Can we write a solution that performs better than linear time?