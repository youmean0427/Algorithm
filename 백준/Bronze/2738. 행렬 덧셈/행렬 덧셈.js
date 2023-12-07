let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

const NM = input[0].split(" ")
const N = parseInt(NM[0])
const M = parseInt(NM[1])

result = []
for (let i = 1; i <= N; i++) {
    let start = input[i].split(" ")
    let end = input[i+N].split(" ")
    let line = []
    for (let j = 0; j < M; j++) {
        a = parseInt(start[j]) + parseInt(end[j])
        line.push(a)
    }
    result.push(line)
}

result.forEach(x => console.log(...x))

