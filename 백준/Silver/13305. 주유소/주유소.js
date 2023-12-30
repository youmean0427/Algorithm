let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const N = parseInt(input[0])
const road = input[1].split(" ").map(x => parseInt(x))
const cost = input[2].split(" ").map(x => parseInt(x))

let minCost = cost[0]
let total = minCost * road[0]

for (let i = 1; i < N-1; i++) {
    minCost = Math.min(minCost, cost[i])
    total += minCost * road[i]
}

console.log(total)