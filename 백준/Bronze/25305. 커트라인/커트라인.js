let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const K = parseInt(input[0].split(" ")[1])

const arr = input[1].split(" ").sort((a, b) => b - a).slice(0, K)
console.log(parseInt(arr[arr.length-1]))