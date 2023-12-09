let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

let arr = new Set()
for (let i = 1; i < input.length; i++) {
    const line = input[i].split(" ")
    const name  = line[0].trim()
    const state = line[1].trim()
    if (state === 'enter') {arr.add(name)}
    if (state === 'leave') {arr.delete(name)}
}

answer = [...arr].sort().reverse()
console.log(answer.join("\n"))