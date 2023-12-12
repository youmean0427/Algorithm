let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

let N = parseInt(input[0])
let arr = input[1].split(" ").map(x => parseInt(x))

stack = []

cnt = 1
while (arr.length) {
    x = arr.shift()
    stack.push(x)

    while (stack.length && stack[stack.length-1] == cnt){
        stack.pop()
        cnt += 1
    }
}

if (stack.length) {
    console.log("Sad")
} else {
    console.log("Nice")
}