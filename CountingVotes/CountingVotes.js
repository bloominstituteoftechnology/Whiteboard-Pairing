
var ary = ['veronica', 'mary', 'alex', 'james', "mary", 'michael', 'alex', 'michael'];

function countVotes(arr) {
    var names = {}
    winner = ""
    record = 0
    for (i=0; i<arr.length; i++) {
      if (!names[arr[i]]) {
        names[arr[i]] = 0
      }
      names[arr[i]] += 1
          if (names[arr[i]] > record) {
        record = names[arr[i]];
        winner = arr[i];
      } else if (names[arr[i]] === record) {
        if (arr[i] > winner) winner = arr[i];
      }
    }
    return(winner)
  }
  
  countVotes(ary)