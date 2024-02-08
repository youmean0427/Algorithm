let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n")

const N = parseInt(input[0])
const arr = input[1].split(" ").map(x => parseInt(x))

let caseArr = []
let visited = new Array(N).fill(0)

function back(n, sm) {

    if (n == N) {
        caseArr.push([...sm])
        return 
    }

    for (let i = 0; i < arr.length; i++) {
        if (visited[i] == 0) {
            sm.push(arr[i])
            visited[i] = 1
            back(n+1, sm)
            visited[i] = 0
            sm.pop()
        }
    }
}

back(0, [])

function check(arr) {
    let result = 0
    for (let i = 0; i < arr.length-1; i++)
        result += Math.abs(arr[i] - arr[i+1])
    return result
}

answer = 0
caseArr.forEach(x => {
    answer = Math.max(answer, check(x))
})

console.log(answer)