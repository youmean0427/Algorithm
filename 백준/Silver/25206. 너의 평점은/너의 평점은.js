let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

const score = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0, "C+" : 2.5, "C0" : 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0.0}

let cnt = 0
let total = 0

for (let i = 0; i < 20; i++) {
    const line = input[i].split(" ")
    let x = parseFloat(line[1])
    let y = parseFloat(score[line[2].trim()])
    // console.log(x * y)

    if (line[2].trim() !== "P") {
        cnt += x
        total += x * y
    }

}
answer = total / cnt
console.log(answer.toFixed(6))