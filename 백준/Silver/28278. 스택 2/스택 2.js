let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')
input = input.map(x => {const line = x.split(" "); return [parseInt(line[0]), parseInt(line[1])]})

let stack = []
let result = []
input.slice(1, ).forEach(x => {
    let n = x[0]

    if (n === 1) {
        stack.push(x[1])
    } else if (n === 2) {
        if (stack.length) {
            x = stack.pop()
            result.push(x)
        } else {
            result.push(-1)
        }
    } else if (n === 3) {
        result.push(stack.length)
    } else if (n === 4) {
        if (stack.length) {
            result.push(0)
        } else {
            result.push(1)
        }
    } else if (n === 5) {
        if (stack.length) {
            result.push(stack[stack.length-1])
        } else {
            result.push(-1)
        }
    }

})
console.log(result.join("\n"))
