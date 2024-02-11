let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n")

function GCD(x, y) {

    while (y > 0) {
        t = x
        x = y
        y = t % y
    }
    return x
}

answer = []
for (let i = 1; i < input.length; i++) {
    line = input[i].split(" ").map(x => parseInt(x))
    answer.push((line[0] * line[1]) / GCD(line[0], line[1]))
}

answer.forEach(x => console.log(x))