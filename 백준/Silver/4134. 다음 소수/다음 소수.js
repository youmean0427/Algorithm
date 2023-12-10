const { Console } = require('console')
let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split('\n')

for (let i = 1; i < parseInt(input[0])+1; i++) {
    let x = parseInt(input[i])
    
    let flag = 1
    
    while (flag) {
        let cnt = 0

        if (x < 2) {
            x++
            continue
        } 
        for (let j = 2; j < parseInt(x ** (1/2)) + 1; j++) {
            if (x % j == 0) {
                cnt = 1
                break
            }
        }
        if (cnt == 0) {
            console.log(x)
            flag = 0
            break
        }
        x++

    }
}