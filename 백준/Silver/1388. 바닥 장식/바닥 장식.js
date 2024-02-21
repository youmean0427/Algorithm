let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split("\n")

const [N, M] = input[0].split(" ").map(x => parseInt(x))
const visited = Array.from({length : N}, () => Array(M).fill(0))
let arr = []

for (let i = 1; i < input.length; i++) {
    arr.push(input[i].trim().split(""))
}

function dfs(sn, sm) {
    let type = 0
    let dir = [0, 0]
    
    if (arr[sn][sm] == "-") {
        type = 1
        dir = [0, 1]
    } else {
        type = 2
        dir = [1, 0]
    }

    let stack = [[sn, sm]]

    while (stack.length) {
        let [x, y] = stack.pop()

        if (visited[x][y] === 0) {
            visited[x][y] = 1

            dx = x + dir[0]
            dy = y + dir[1]

            if (0 <= dx && dx < N && 0 <= dy && dy < M) {
                if (visited[dx][dy] === 0) {
                    if ((type === 1 && arr[dx][dy] === '-') || (type === 2 && arr[dx][dy] === '|')) {
                        stack.push([dx, dy])
                    }
                }
            }
        }
    }
}

let ans = 0
for (let a = 0; a < N; a++) {
    for (let b = 0; b < M; b++) {
        if (visited[a][b] === 0) {
            dfs(a, b)
            ans += 1
        }
    }
}

console.log(ans)