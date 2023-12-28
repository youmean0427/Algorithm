let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
//let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")

const N = parseInt(input[0])

const arr = input[1].split(" ").map(x => parseInt(x))
const op = input[2].split(" ").map(x => parseInt(x))

let max = -Infinity
let min = Infinity
function back(n, sm) {
    
    if (n >= N) {
        max = Math.max(sm, max)
        min = Math.min(sm, min)
        return
    }

    for (let i = 0; i < op.length; i++) {
        if (op[i]) {
            op[i] -= 1

            if (i === 0) {
                
                back(n+1, sm+arr[n])
              
            } else if (i === 1) {
       
                back(n+1, sm-arr[n])
       
            } else if (i === 2) {
          
                back(n+1, sm*arr[n])
           
            } else if (i === 3) {
          
                if (sm < 0) {
                    back(n+1, -parseInt(-sm / arr[n]))
                } else {
                    back(n+1, parseInt(sm / arr[n]))
                }
              
            }
            op[i] += 1
        }
    }
}

back(1, arr[0])
console.log(max === -0 ? 0 : max)
console.log(min === -0 ? 0 : min)