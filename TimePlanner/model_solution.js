function timePlanner(a, b, duration) {
  let aCount = 0;
  let bCount = 0;

  while (aCount < a.length && bCount < b.length) {
    const start = Math.max(a[aCount][0], b[bCount][0]);
    const end = Math.min(a[aCount][1], b[bCount][1]);

    if (start + duration <= end) {
      return [start, start + duration];
    }

    if (a[aCount][1] < b[bCount][1]) {
      aCount++;
    } else {
      bCount++;
    }
  }

  return [];
}

/* Some simple console.log tests */
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