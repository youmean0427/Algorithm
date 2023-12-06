let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// /dev/stdin 
// ./EX.txt

const line = input[0].split(" ")
const N = line[0]
const M = line[1]

let arr = new Array(parseInt(N)).fill(0)

for (let i = 1; i <= parseInt(M); i++) {
    let info = input[i].split(" ")
    let start = parseInt(info[0])
    let end = parseInt(info[1])
    let num = parseInt(info[2])
    for (let j = start-1; j <= end-1; j++) {
        arr[j] = num
    }
}
console.log(...arr)