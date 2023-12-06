let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// const input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

input.forEach(x => console.log(x))