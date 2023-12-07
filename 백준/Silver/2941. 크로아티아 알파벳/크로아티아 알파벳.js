let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim()
// let input = fs.readFileSync("./EX.txt").toString().trim()
alpha = ["c=", 'c-', "dz=", "d-", "lj", "nj", "s=", "z="]

for (i of alpha) {
    input = input.replaceAll(i, "*") 
}
console.log(input.length)