let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim()
// const input = fs.readFileSync("./EX.txt").toString().trim()

let N = Number(input)

let i = 1
let minus = 2
let cnt = 1
let answer = ""

while (cnt <= 2*N - 1) {
    answer += " ".repeat(N-i) + "*".repeat(2*i-1) + "\n"
    
    if (cnt >= N) {
        i = cnt + 1 - minus
        minus += 2
    }
    else {
        i += 1
    }
    cnt += 1
}

console.log(answer)