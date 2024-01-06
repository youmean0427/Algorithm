let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('./EX.txt').toString().trim().split('\n')
const [N, M] = input[0].split(" ").map(x => parseInt(x))

const p = []
for (let i = 0; i < N; i++) {
    p.push(i)
}

function find_set(x) {
    if (p[x] !== x) {
        p[x] = find_set(p[x])
    } 
    return p[x]
}


let cnt = M + 1
function union(x, y, i) {
    let xp = find_set(x)
    let yp = find_set(y)
    if (xp === yp) {
        cnt = Math.min(cnt, i)
        return
    } else if (xp < yp) {
        p[yp] = xp
    } else {
        p[xp] = yp
    }
}

for (let i = 1; i < input.length; i++) {
    const line = input[i].split(" ").map(x => parseInt(x))
    union(line[0], line[1], i)
}

{cnt === M+1 ? console.log(0) : console.log(cnt)}