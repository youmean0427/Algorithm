let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

let answer = 0

if (input[0] === input[1] && input[1] === input[2]) {
    answer = 10000 + parseInt(input[0]) * 1000
} else if (input[0] === input[1] || input[1] === input[2]) {
    answer = 1000 + parseInt(input[1]) * 100
} else if (input[0] === input[2]) {
    answer = 1000 + parseInt(input[2]) * 100
} else {
    input.sort((a, b) => b - a)
    answer = parseInt(input[0]) * 100
}

console.log(answer)
