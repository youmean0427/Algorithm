let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('./EX.txt').toString().trim().split('\n')
const T = parseInt(input[0])

// bfs
function bfs(x, y, L, n, m) {
    let q = [[x, y]]
    if (x === n && y === m) {
        return 0;
    }
    let visited = Array.from({length: L}, () => Array(L).fill(0))
    visited[x][y] = 1
    while (q.length) {
        
        let line = q.shift()
        let xx = line[0]
        let yy = line[1]
        
        let dir = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
        dir.forEach(x => {
            let xn = xx + x[0]
            let ym = yy + x[1]
            if (0 <= xn && xn < L && 0 <= ym && ym < L) {
                if (visited[xn][ym] === 0) {
                    visited[xn][ym] += visited[xx][yy] + 1
                    q.push([xn, ym])
                }
            }

        })
    }
    return visited[n][m]-1
}



let i = 1
while (i <= T*3) {
    const L = parseInt(input[i])
    let [x, y] = input[i+1].split(" ").map(x => parseInt(x))
    let [n, m] = input[i+2].split(" ").map(x => parseInt(x))
    // let arr = Array.from({length : L}, () => Array(L).fill(0))
    let ans = bfs(x, y, L, n, m)
    console.log(parseInt(ans))
    i += 3
} 