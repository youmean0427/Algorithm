let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim()

const N = parseInt(input)
let i = 1
let answer = "long int" 
while (i < N / 4) {
    answer = "long " + answer
    i++
}
console.log(answer)