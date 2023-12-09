let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")


input = input.map(x => parseInt(x)).sort((a, b) => a - b)
console.log(input.reduce((a, b) => a + b) / 5)
console.log(input[2])
