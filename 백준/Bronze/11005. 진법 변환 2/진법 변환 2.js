let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")
// let input = fs.readFileSync("./EX.txt").toString().trim().split(" ")

let N = parseInt(input[0])
const B = parseInt(input[1]) 
const arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

const x = []

while (N >= B) {
    x.push(N % B)
    N = parseInt(N / B)
}

x.push(N)
x.reverse()

let answer = ''
x.forEach(x => {answer += arr[x]})
console.log(answer)