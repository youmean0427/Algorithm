let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

input = input.map(x => parseInt(x))
cost = [25, 10, 5, 1]
result = [0, 0, 0, 0]
input.forEach((x, idx) => {
    if (idx !== 0) {
        for (let i = 0; i < 4; i++) {
            result[i] = Math.trunc(x / cost[i])
            x %= cost[i]
        }
        console.log(...result)
    }
   
})

