let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")
const N = input.length

function divisor(x) {
    let answer = x + ' = ' + '1'
    let total  = 1
    
    for (let i = 2; i < x; i++ ){
        if (x % i == 0) {
            total += i
            answer += ' + '
            answer += i
        }
    }
    
    if (total == x) {
        return answer
    } else {
        answer = x + " is NOT perfect."
        return answer
    }
}

for (let i = 0; i < N; i++ ) {
    if (input[i] != -1) {
        answer = divisor(input[i])
        console.log(answer)
    }
}