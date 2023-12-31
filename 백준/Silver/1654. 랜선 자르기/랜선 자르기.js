let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const N = parseInt(input[0].split(" ")[0])
const K = parseInt(input[0].split(" ")[1])

const arr = input.slice(1, ).map(x => parseInt(x))

let start = 1
let end = Math.max(...arr)
let result = 0
while (start <= end) {
    let cnt = 0
    let mid = Math.trunc((start + end) / 2)
    for (let i = 0; i < arr.length; i++) {
        cnt += Math.trunc(arr[i] / mid)
    }
    if (cnt < K) {
        end = mid - 1
    } else {
        start = mid + 1
    }
}
console.log(end)