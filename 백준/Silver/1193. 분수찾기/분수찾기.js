let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim()
// let input = fs.readFileSync("./EX.txt").toString().trim()

const X = parseInt(input)
let line = 0
let total = 0

while (total < X) {
    line += 1
    total += line
}

const start = (X - (total - line ))

n = 1
m = line

if (line % 2 == 0){
    for (let a = 1; a < start; a++) {
        n += 1
        m -= 1
    }
    console.log(`${n}/${m}`)
} else {
    for (let a = line; a > start; a--) {
        n += 1
        m -= 1
    }
    console.log(`${n}/${m}`)
}