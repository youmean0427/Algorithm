let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('./EX.txt').toString().trim().split('\n')

const S = input[0].trim()
const B = input[1].trim()


let stack = []
let start = 0
for (let i = 0; i < S.length; i++) {
    stack.push(S[i])
    
    if (stack.slice(stack.length-B.length,stack.length).join("") === B) {
        stack.splice(stack.length-B.length, B.length)
    }

}
if (stack.length) {
    console.log(stack.join(""))
} else {
    console.log("FRULA")
}
