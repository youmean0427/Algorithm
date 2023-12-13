let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

function PALINDROM(x, start, end, cnt) {
    cnt += 1
    if (start >= end) {
        return [1, cnt]
    } else if (x[start] !== x[end]) {
        return [0, cnt]
    } else {
        return PALINDROM(x, start+1, end-1, cnt)
    }
}

result = ""
for (let i = 1; i < input.length; i++) {
    s = input[i].trim()
    x = PALINDROM(s, 0, s.length-1, 0 )
    result += x.join(" ") + "\n"
}
console.log(result)