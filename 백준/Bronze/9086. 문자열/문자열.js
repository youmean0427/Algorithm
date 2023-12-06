let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// const input = fs.readFileSync("./EX.txt").toString().trim().split("\n")
const T = parseInt(input[0])
let i = 1

while (i <= T) {
    const S = input[i].trim()
    console.log(S[0]+S[S.length-1])
    
    i++
}
