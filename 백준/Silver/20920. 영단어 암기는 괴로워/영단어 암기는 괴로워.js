let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

const M = parseInt(input[0].split(" ")[1])
let arr = new Map()
for (let i = 1; i < input.length; i++) {
    let x = input[i].trim()

    if (x.length >= M) {
        arr.set(x, (arr.get(x) ?? 0 ) + 1)
    }
} 

arr = [...arr.entries()].sort((x, y) => {
    if (x[1] !== y[1]) return y[1] - x[1]
    if (x[0].length !== y[0].length) return y[0].length - x[0].length
    return x[0].localeCompare(y[0])
}).map(x => x[0])


console.log(arr.join("\n"))