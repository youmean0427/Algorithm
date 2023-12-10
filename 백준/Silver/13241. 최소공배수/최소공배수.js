let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")
// let input = fs.readFileSync("./EX.txt").toString().trim().split(" ")


function GCD (a, b) {
    while (b > 0) {
        aa = a
        a = b
        b = aa % b
    }
    return a
}

function LCM (a, b) {
    return a * b / GCD(a, b)
}

const A = parseInt(input[0])
const B = parseInt(input[1])
console.log(parseInt(LCM(A, B)))