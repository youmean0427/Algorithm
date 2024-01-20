let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split("")
// let input = fs.readFileSync('./EX.txt').toString().trim().split("")

const korea = "KOREA"
let kIdx = 0
const yonsei = "YONSEI"
let yIdx = 0

while (input.length) {
    let x = input.shift()

    if (x === korea[kIdx]) {{
        kIdx += 1
    }}
    if (x === yonsei[yIdx]) {
        yIdx += 1
    }

    if (kIdx === 5){
        answer = korea
        break
    } else if (yIdx === 6) {
        answer = yonsei
        break
    }
}
console.log(answer)