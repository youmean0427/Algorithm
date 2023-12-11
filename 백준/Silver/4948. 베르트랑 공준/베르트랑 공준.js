const { Console } = require('console')
let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

input = input.map(x => parseInt(x))

function check(start, end){
    let arr = new Array(end+1).fill(true)
    
    for (let i = 2; i < parseInt(end ** 0.5)+1; i++) {
        if (arr[i]) {
            for (let j = 2*i; j < end+1; j+=i) {
                arr[j] = false
            }
        }
    }

    let cnt = 0
    for (k of arr.slice(start+1, end+1)) {
        if (k) {
            cnt += 1
        }
    }
    return cnt 
}

input.forEach(x => {if (x !== 0) {console.log(check(x, 2*x))}})