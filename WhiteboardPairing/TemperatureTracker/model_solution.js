class TempTracker {
  constructor() {
    // for mode
    // populate occurrences array with 0s from 0 to 140
    // 140 being the max temperature 
    this.occurrences = Array(140).fill(0);
    this.maxOccurrences = 0;
    this.mode = null;

    // for mean
    this.numberOfReadings = 0;
    this.totalSum = 0;
    this.mean = null;

    // for min and max
    this.minTemp = null;
    this.maxTemp = null;
  }

  insert(temp) {
    // for mode
    // increment the number of times this temp has appeared
    this.occurrences[temp]++;
    // update our maxOccurences and mode variables if necessary
    if (this.occurrences[temp] > this.maxOccurrences) {
      this.mode = temp;
      this.maxOccurrences = this.occurrences[temp];
    }

    // for mean
    this.numberOfReadings++;
    this.totalSum += temp;
    this.mean = this.totalSum / this.numberOfReadings;

    // for min and max
    if (this.maxTemp === null || temp > this.maxTemp) {
      this.maxTemp = temp;
    }
    if (this.minTemp === null || temp < this.minTemp) {
        this.minTemp = temp;
    }
  }

  getMax() {
    return this.maxTemp;
  }

  getMin() {
    return this.minTemp;
  }

  getMean() {
    return this.mean;
  }

  getMode() {
    return this.mode;
  }
}

/* Some console.log tests */
const tracker = new TempTracker();
tracker.insert(32);

console.log("mean: ", tracker.getMean());   // should print 32
console.log("min: ", tracker.getMin());     // should print 32
console.log("max: ", tracker.getMax());     // should print 32
console.log("mode: ", tracker.getMode());   // should print 32

tracker.insert(135);

console.log("mean: ", tracker.getMean());   // should print 83.5
console.log("min: ", tracker.getMin());     // should print 32
console.log("max: ", tracker.getMax());     // should print 135

tracker.insert(135);

console.log("mean: ", tracker.getMean());   // should print 100.66666666666667
console.log("min: ", tracker.getMin());     // should print 32
console.log("max: ", tracker.getMax());     // should print 135
console.log("mode: ", tracker.getMode());   // should print 135