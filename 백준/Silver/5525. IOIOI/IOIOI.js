let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const N = parseInt(input[0])
const M = parseInt(input[1])
const S = input[2]

const len = 2 * N + 1

let i = 0
let cnt = 0
let ans = 0

while (i < M){

    x = S[i] + S[i+1] + S[i+2]

    if (x === "IOI") {
        cnt += 1
        if (cnt === N) {
            ans += 1
            cnt -= 1
        }
        i += 2
        
    } else {
        i += 1
        cnt = 0
    }

}

console.log(ans)