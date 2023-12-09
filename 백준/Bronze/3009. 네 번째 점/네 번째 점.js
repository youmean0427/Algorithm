let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

let x = {}
let y = {}
for (let i = 0; i < 3; i++) {
    const line = input[i].split(" ")
    const n = parseInt(line[0])
    const m = parseInt(line[1])

    if (n in x) {
        x[n] += 1
    } else {
        x[n] = 1
    }

    if (m in y) {
        y[m] += 1
    } else {
        y[m] = 1
    }


}

const xArr = Object.entries(x)
const yArr = Object.entries(y)

xArr.sort((a, b) => a[1] - b[1])
yArr.sort((a, b) => a[1] - b[1])
console.log(xArr[0][0], yArr[0][0])