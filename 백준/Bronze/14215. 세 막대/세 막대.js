let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")
// let input = fs.readFileSync("./EX.txt").toString().trim().split(" ")

input = input.map(x => parseInt(x))
input.sort((a, b) => a - b)

val = input[0] + input[1]
if (val <= input[input.length-1]) {
    console.log(2 * val - 1)
} else {
    const sum = input.reduce((a, b) => a + b )
    console.log(sum)
}