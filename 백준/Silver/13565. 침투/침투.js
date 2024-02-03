let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')

const [N, M] = input[0].split(" ").map(x => parseInt(x))
let arr = []
for (let i = 1; i < input.length; i++) {
    arr.push([...input[i].trim()].map(x => parseInt(x)))
}
visited = Array.from({length : N}, () => Array(M).fill(0))

function dfs(n, m) {
    let stack = [[n, m]]

    while (stack.length) {

        const p = stack.pop()
        let x = p[0]
        let y = p[1]
        if (x === N-1) {
            return true
        }

        if (arr[x][y] === 0 && visited[x][y] === 0) {
            visited[x][y] = 1
            const dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for (d of dir) {
                xd = x + d[0]
                yd = y + d[1]
                
                if (xd >= 0 && xd < N && yd >= 0 && yd < M) {
                    if (visited[xd][yd] == 0 && arr[xd][yd] == 0) {
                        stack.push([xd, yd])
                    }
                }
            }
        }
    }
}

answer = "NO"
for(let i = 0; i < M; i++) {
    if (dfs(0, i)) {
        answer = "YES"
        break
    }
}
console.log(answer)
