let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('./EX.txt').toString().trim().split('\n')

const [N, M, R] = input[0].split(" ").map(x => parseInt(x))
let arr = Array.from({length : N+1}, () => [])

for (let i = 1; i <= M; i++) {
    const [a, b] = input[i].split(" ").map(x => parseInt(x))
    arr[a].push(b)
    arr[b].push(a)
}

function bfs(x) {
    
    let visited = Array(N+1).fill(0)

    let q = [x]
    let cnt = 1
    while (q.length) {
        let y = q.shift()


        if (visited[y] === 0) {
            visited[y] = cnt
        }
        arr[y].sort((a, b) => a - b)
        // console.log(arr[y])
        arr[y].forEach(x => {
            if (visited[x] === 0) {
                visited[x] = cnt + 1
                q.push(x)
                cnt += 1
            }
        })
    }
    return visited
}

result = bfs(R)
ans = ''
for (let i = 1; i < result.length; i++) {
    ans += result[i] + '\n'
}
console.log(ans)