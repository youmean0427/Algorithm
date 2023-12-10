let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim()
// let input = fs.readFileSync("./EX.txt").toString().trim()

const S = input.trim()
let S_set = new Set()

let i = 0
let j = 1

while (i < S.length) {
    while(j < S.length+1) {
        S_set.add(S.slice(i, j))
        j ++
    }
    i++
    j = i+1
}

console.log(S_set.size)