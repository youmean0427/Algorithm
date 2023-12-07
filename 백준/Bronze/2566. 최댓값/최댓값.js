let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split('\n')
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

let maxVal = 0
let ij = [1, 1]
for (let i = 0; i < 9; i++) {
    let line = input[i].split(" ")   
    line.forEach((x, idx) => {
            if (parseInt(x) > maxVal) {
                maxVal = parseInt(x) 
                ij[0] = i+1
                ij[1] = idx+1
            }
        }
    )
}
console.log(maxVal)
console.log(...ij)