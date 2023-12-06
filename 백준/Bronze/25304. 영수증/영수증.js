let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

X = input[0]
N = input[1]

let total = 0
for (let i = 2; i < input.length; i++) {
    line = input[i].split(" ")
    total += parseInt(line[0]) * parseInt(line[1])
}

if (parseInt(X) === total) {
    console.log("Yes")
} else {
    console.log("No")
}