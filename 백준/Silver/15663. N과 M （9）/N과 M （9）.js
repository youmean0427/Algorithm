let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('./EX.txt').toString().trim().split("\n")

const [n, m] = input[0].split(" ").map((x) => parseInt(x))
const arr = input[1].split(" ").map(x => parseInt(x))
let visited = new Array(n).fill(0)
arr.sort((a, b) => a - b)
result = []

function dfs(x, sm){
    
    if (sm.length === m) {
        result.push(sm)
        return
    }

    for (let i = 0; i < n; i++) {
        if (visited[i] === 0) {
            visited[i] = 1
            dfs(i, [...sm , arr[i].toString()])
            visited[i] = 0
        }
    }
}

dfs(0, [])
let answer = {}
for (let  i =0 ; i < result.length; i++) {
    answer[[result[i]]] = 1
}

ans = ""
Object.keys(answer).forEach(x => { ans += x.split(",").join(" ") + '\n'} )
console.log(ans)