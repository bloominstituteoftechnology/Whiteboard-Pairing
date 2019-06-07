function timePlanner(a, b, duration) {
  // keep track of which range of times in `a` or `b` 
  // we are currently exploring
  let aCount = 0;
  let bCount = 0;

  // as long as we have not run out of time ranges to explore
  while (aCount < a.length && bCount < b.length) {
    // given two specific time ranges, identify the overlapping period (if any) 
    // which is bounded by the latest start time and earliest end time
    // (drawing out one of the examples on a timeline can help visualize this)
    const start = Math.max(a[aCount][0], b[bCount][0]);
    const end = Math.min(a[aCount][1], b[bCount][1]);

    // if the meeting will not go longer than the `end` of the overlapping 
    // period, return the meeting start and end times
    if (start + duration <= end) {
      return [start, start + duration];
    }

    // else, choose the next time range with which to repeat the above process
    // (if an example drawn out, can think of this as moving along the 
    // timeline, until the next time range hit)
    if (a[aCount][1] < b[bCount][1]) {
      aCount++;
    } else {
      bCount++;
    }
  }

  return [];
}

// Tests
console.log(timePlanner(
  [[10, 50], [60, 120], [140, 210]],
  [[0, 15], [60, 70]],
  8
));   // should print [60, 68]

console.log(timePlanner(
  [[10, 50], [60, 120], [140, 210]],
  [[0, 15], [60, 72]],
  12
));   // should print [60, 72]

console.log(timePlanner(
  [[10, 50], [60, 120], [140, 210]],
  [[0, 15], [60, 70]],
  12
));   // should print []

console.log(timePlanner(
  [[0, 5], [50, 70], [120, 125]],
  [[0, 50]],
  8
));   // should print []
