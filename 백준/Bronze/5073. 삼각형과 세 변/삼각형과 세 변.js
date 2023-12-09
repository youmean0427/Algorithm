let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

for (let i = 0; i < input.length-1; i++) {
    const line = input[i].split(" ")
    const a = parseInt(line[0])
    const b = parseInt(line[1])
    const c = parseInt(line[2])
    const arr = [a, b, c]
    if (a === 0) {
        break
    }

    arr.sort((a, b) => a - b)
    
    if (arr[arr.length-1] < arr[0] + arr[1]) {
        if (a === b && b === c) {
            console.log("Equilateral")
        } else if (a === b || b === c || a === c) {
            console.log("Isosceles")
        } else {
            console.log("Scalene")
        }
    } else {
        console.log("Invalid")
    }
    

}