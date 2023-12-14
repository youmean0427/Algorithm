let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

input = input.map(x => parseInt(x))

function cantor(x, start, end){
    if (start < end) {
        let mid = parseInt((end - start + 1) / 3)
        x.fill(' ', start + mid, start + 2 * mid);
        // x.splice(start + mid, mid, ...Array(mid).fill(' '));
        cantor(x, start, start + mid - 1)
        cantor(x, start + 2 * mid, end)
    }
}

for(let i = 0; i < input.length; i++) {
    let N = input[i]
    let arr = new Array(3 ** N).fill('-')
    cantor(arr, 0, arr.length-1)
    console.log(arr.join(""))
}

