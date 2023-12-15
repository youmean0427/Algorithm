let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")
// let input = fs.readFileSync("./EX.txt").toString().trim().split(" ")

const N = parseInt(input[0])
const M = parseInt(input[1])

let result = []
function nm(n, sm) {

    if (n == M) {
        result.push(sm)
        return
    }

    for (let i = 1; i < N+1; i++) {
        if (sm.includes(i.toString())) {
            continue
        } else {
            nm(n+1, sm + i.toString())
        }
    }
}

nm(0, "")
let answer = ''
result.forEach(x => answer += (x.split("").join(" ")) + "\n")
console.log(answer)