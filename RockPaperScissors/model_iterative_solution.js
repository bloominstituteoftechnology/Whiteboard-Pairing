/**
 * Time Complexity  : O(3^n)
 * Space Complexity : O(3^n)
 * 
 * If the code is confusing, insert this
 * console.log between lines 21-22 ->
 * console.log('pointers =', pointers);
 * 
 * Credits: William Connaster (WilliamConnatser),
 *          Samuel Ko (samsisle)
 */

function rockPaperScissors(n) {
  // Outcomes array is the outer array that
  // will hold all of the unique outcomes.
  let outcomes = [];
  const plays = ["rock", "paper", "scissors"];

  let pointers = Array(n).fill(0);
  let pointer = n - 1;

  while (pointers[0] !== 3) {
    // Push an outcome, then increment the pointer.
    // For example: [0,0] -> push -> [0,1]...
    while (pointers[pointer] < 3) {
      outcomes.push(pointers.map(i => plays[i]));
      pointers[pointer]++;
    }

    // Move the pointer to the left. If the pointer is equal to
    // 2, then update the pointer value to 0. Keep moving to the
    // left until the pointer value is not equal to 2.
    do {
      pointers[pointer] = 0;
      pointer--;
    } while (pointers[pointer] === 2 && pointer > 0);

    // Increment the value at pointer, then restart the loop
    // with the pointer at the end of the pointers array.
    pointers[pointer]++;
    pointer = n - 1;
  }

  return outcomes;
}

/* Some console.log tests */
const rv1 = rockPaperScissors(2);
console.log(rv1); // should print [[rock, rock], [rock, paper], [rock, scissors], [paper, rock], [paper, paper], [paper, scissors], [scissors, rock], [scissors, paper], [scissors, scissors]]

const rv2 = rockPaperScissors(3);
console.log(rv2.length); // should print 27

const rv3 = rockPaperScissors(4);
console.log(rv3.length); // should print 81

const rv4 = rockPaperScissors(5);
console.log(rv4.length); // should print 243
