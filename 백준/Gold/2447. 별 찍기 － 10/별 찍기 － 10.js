let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim()

const N = parseInt(input)
const arr = Array.from({ length: N }, () => Array(N).fill('*'));

function star(x, start, end, N) {
    if (N >= 3) { 
        for (let i = start+parseInt(N/3); i < (start + 2 * parseInt(N/3)); i++) {
            for (let j  = end+parseInt(N/3); j < (end + 2 * parseInt(N/3)); j++) {
                x[i][j] = " "
            }
        }
        
        for (let n = start; n < start + N; n += parseInt(N/3)) {
            for (let m = end; m < end + N; m += parseInt(N/3)) {
                star(x, n, m, parseInt(N/3))
            }
        }
    }
}

star(arr, 0, 0, N)
let answer = ''
arr.forEach(x => {
    answer += x.join("") + "\n"

})
console.log(answer)