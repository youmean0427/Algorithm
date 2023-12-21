let fs = require('fs')
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n")
// let input = fs.readFileSync("./EX.txt").toString().trim().split("\n")


const N = parseInt(input[0].split(" ")[0])
const M = parseInt(input[0].split(" ")[1])

arr = new Array(101).fill(0)
for (let i = 1; i < input.length; i++) {
    let line = input[i].split(" ").map(x => parseInt(x))
    arr[line[0]] = line[1]
}

let visited = new Array(101).fill(Infinity)
visited[1] = 0
function bfs(start) {
    
    let q = [start]
    while (q.length) {

        let x = q.shift()
        
        if (x == 100) {
            return
        }

        for (let i = 1; i < 7; i++) {
           let y = x + i 
           if (visited[y] > visited[x] + 1) {
                visited[y] = Math.min(visited[y], visited[x]+ 1)
                if (arr[y]) {
                    q.push(arr[y])
                    visited[arr[y]] = Math.min(visited[arr[y]], visited[x]+ 1)
                } else {
                    q.push(y)
                }
            }
        }
    }  
}

bfs(1)
console.log(visited[100])