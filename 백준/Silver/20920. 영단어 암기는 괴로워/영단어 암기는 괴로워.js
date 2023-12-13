let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

const M = parseInt(input[0].split(" ")[1])
let arr = {}
for (let i = 1; i < input.length; i++) {
    let x = input[i].trim()
    
    if (x.length >= M) {
        if (x in arr) {
            arr[x] += 1
        } else {
            arr[x] = 1
        }
    }
} 

arr = Object.entries(arr)
arr.sort((x, y) => {
    if (x[1] > y[1]) return -1
    if (x[1] < y[1]) return 1
    if (x[0].length > y[0].length) return -1
    if (x[0].length < y[0].length) return 1
    if (x[0] > y[0]) return 1
    if (x[0] < y[0]) return -1
    return 1
})

arr = arr.map(x => x[0])
console.log(arr.join("\n"))