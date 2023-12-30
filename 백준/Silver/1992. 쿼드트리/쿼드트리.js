let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const N = parseInt(input[0])
let arr = []
for (let i = 1; i < input.length; i++) {
    arr.push(input[i].trim().split("").map(x => parseInt(x)))
}
let result = []

function quadTree(x, y, T){
    
    if (T == 1) {
        result.push(arr[x][y])
        return
    }

    zeroCnt = 0
    oneCnt = 0
    for (let i = x; i < x+T; i++) {
        for (let j = y; j < y+T; j++) {
            if (arr[i][j]) {
                oneCnt += 1
            } else {
                zeroCnt += 1
            }
        }
    }
   
    if (zeroCnt === T*T) {
        result.push(0)
        return
    } else if (oneCnt === T*T) {
        result.push(1)
        return
    } else {
        result.push('(')
        quadTree(x, y, T/2)
        quadTree(x, y+T/2, T/2)
        quadTree(x+T/2, y, T/2)
        quadTree(x+T/2, y+T/2, T/2)
        result.push(')')
    }
}
quadTree(0, 0, N)
console.log(result.join(""))