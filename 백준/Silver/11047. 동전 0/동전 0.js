let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const info = input[0].split(" ").map(x => parseInt(x))
const N = info[0]
let K = info[1]

const A = input.slice(1, ).map(x => parseInt(x)).reverse()
cnt = 0
for (let i of A) {
    if (K >= i) {
        cnt += Math.floor(K / i) 
        K = K % i
    }
}
console.log(cnt)