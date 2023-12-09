let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")
// let input = fs.readFileSync("./EX.txt").toString().trim().split(" ")
const N = parseInt(input)
let arr = []
function fin(N){
    for (let i = 2; i <= N; i++) {
        if (N % i == 0) {
            a = i
            arr.push(a)
            break
        }
    }
    b = parseInt(N / a)
    if (b > a) {
        fin(b)
    } else if (b != 1) {
        arr.push(b)
    }
}

if (N != 1) {
    fin(N)
    arr.forEach(x => console.log(x))
}