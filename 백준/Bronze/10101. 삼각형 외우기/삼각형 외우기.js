let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

let arr = []
let total = 0
input.forEach(x => {
    const num = parseInt(x)
    if (arr.includes(num) === false) {
        arr.push(num)
        total += num
    } else {
        total += num
    }
})

if (total === 180) {
    if (arr.length === 1) {
        console.log("Equilateral")
    } else if (arr.length === 2) {
        console.log("Isosceles")
    } else {
        console.log("Scalene")
    }
} else {
    console.log("Error")
}