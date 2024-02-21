let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n")

let S = input[0]
answer = ''
for(let i = 0; i < S.length; i += 10) {
    answer += S.slice(i, i+10) + '\n'
}
console.log(answer)
