let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// console.log(input)

const N = input[0]
let i = 1
let answer = ''
while (i <= N) {
    const line = input[i].split(" ")
    answer += parseInt(line[0]) + parseInt(line[1]) + "\n"
    i++
} 

console.log(answer)