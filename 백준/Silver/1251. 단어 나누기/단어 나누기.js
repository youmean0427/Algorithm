let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split("")

let answer = []
for (let i = 1; i < input.length; i++) {
    for (let j = i+1; j < input.length; j++ ) {
        let a = input.slice(0, i).reverse().join("")
        let b = input.slice(i, j).reverse().join("")
        let c = input.slice(j, input.length).reverse().join("")
        answer.push(a+b+c)        
    }
}
answer.sort()
console.log(answer[0])
