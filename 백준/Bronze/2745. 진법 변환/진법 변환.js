let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")
// let input = fs.readFileSync("./EX.txt").toString().trim().split(" ")

console.log(parseInt(input[0], parseInt(input[1])))