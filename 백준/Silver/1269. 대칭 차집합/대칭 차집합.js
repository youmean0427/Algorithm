let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const aArr = input[1].split(" ").map(x => parseInt(x))
const bArr = input[2].split(" ").map(x => parseInt(x))

let a = new Set(aArr)
let b = new Set(bArr)

let ab = [...a].filter(x => !b.has(x))
let ba = [...b].filter(x => !a.has(x))

console.log(ab.length + ba.length)