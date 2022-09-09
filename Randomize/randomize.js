var ary = [1, 2, 3, 4]

function randomize(arr) {
  arr.forEach((item, i) => {
    var randoSpot = Math.floor(Math.random() * arr.length)
    var temp = arr[i]
    arr[i] = arr[randoSpot]
    arr[randoSpot] = temp
    console.log(randoSpot)
  })
}

randomize(ary)

console.log(ary)