const { Console } = require('console')
let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

const a = parseInt(input[0].split(" ")[0])
const b = parseInt(input[0].split(" ")[1])
const c = parseInt(input[1].split(" ")[0])
const d = parseInt(input[1].split(" ")[1])

function GCD(a, b) {
    while (b > 0) {
        aa = b
        b = a % b
        a = aa
    }
    return a
}

function LCM(a, b) {
    return a * b / GCD(a, b)
}

m = parseInt(LCM(b, d))
n = parseInt(a * (m / b) + c * (m / d))
k = GCD(n, m)
console.log(n / k, m / k )