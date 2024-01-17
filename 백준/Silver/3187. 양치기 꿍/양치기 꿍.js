let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('./EX.txt').toString().trim().split("\n")
const [R, C] = input[0].split(" ").map(x => parseInt(x))

arr = []
for (let i = 1; i < input.length; i++) {
    arr.push(input[i].split(""))
}
visited = Array.from({length:R}, () => (new Array(C).fill(0)))

function dfs(x, y) {

    let stack = [[parseInt(x), parseInt(y)]]
    let [s, w] = [0, 0]
    visited[s][w] = 0
    while (stack.length) {
        const [a, b] = stack.pop()

        const dir = [[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]]

        for (let d of dir) {
            n = a + d[0]
            m = b + d[1]
            if (n >= 0 && n < R && m >= 0 && m < C) {
                
                if (visited[n][m] === 0 && arr[n][m] !== '#') {
                    if (arr[n][m] === 'k') {
                        s += 1
                    } else if ( arr[n][m] === 'v' ) {
                        w += 1
                    } 
                    visited[n][m] = 1
                    stack.push([n, m])
                    }
                }
            }
        }
    return [s, w]
}


let [ans1, ans2] = [0, 0]
for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
        if (arr[i][j] !== '#' && visited[i][j] === 0) {
            [x, y]= dfs(i, j)
            
            if (x > y) {
                y = 0
            } else {
                x = 0
            }
            ans1 += x
            ans2 += y
        } 
    }
}

console.log(ans1, ans2)


