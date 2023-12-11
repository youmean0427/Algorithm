let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')
input = input.map(x => parseInt(x))

function prime(x) {
    arr = new Array(x).fill(true)
    for (let i = 2; i < x; i++) {
        if (arr[i]) {
            for (let j = i+i; j < x; j += i) {
                arr[j] = false
            }
        }
    }
    return arr
}

const p = prime(1000000)

input.forEach((x, i) => {
    if (i !== 0) {
        let cnt = 0
        for (let j = 2; j < parseInt(x/2)+1; j++) {
            if (p[j] && p[x-j]) {
                cnt += 1
            }
        }
        console.log(cnt)
}})
