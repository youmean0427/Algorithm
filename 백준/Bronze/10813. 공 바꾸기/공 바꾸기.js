let fs = require('fs')
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// /dev/stdin 
// ./EX.txt

const line = input[0].split(" ").map(x => parseInt(x))
const N = line[0]
const M = line[1]

let arr = []
for (let i = 0; i <= N; i++) {
    arr.push(i)
}

cnt = 1
while (cnt <= M) {
    const balls = input[cnt].split(" ").map(x => parseInt(x))
    a = balls[0]
    b = balls[1]
    
    x = arr[a]
    y = arr[b]

    arr[a] = y
    arr[b] = x
    
    cnt++
}
result = arr.slice(1,)
console.log(...result)
