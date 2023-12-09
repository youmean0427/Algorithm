let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")
// let input = fs.readFileSync("./EX.txt").toString().trim().split(" ")


input = input.map(x => parseInt(x))

const y = (input[2] * input[3] - input[5] * input[0]) / (input[1] * input[3] - input[4] * input[0])
const x = (input[2] * input[4] - input[1] * input[5]) / (input[0] * input[4] - input[1] * input[3])

console.log(parseInt(x), parseInt(y))