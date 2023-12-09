let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const N = parseInt(input[0])

xMax = -Infinity
xMin = Infinity
yMax = -Infinity
yMin = Infinity

if (N !== 1) {
    for (let i = 1; i <= N; i++) {
        const line = input[i].split(" ")
        const a = parseInt(line[0])
        const b = parseInt(line[1])

        xMax = Math.max(xMax, a)
        xMin = Math.min(xMin, a)
        yMax = Math.max(yMax, b)
        yMin = Math.min(yMin, b)
    }

    console.log((xMax - xMin) * (yMax - yMin))
} else {
    console.log(0)
}