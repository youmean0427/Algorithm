let fs = require("fs")
let input = fs.readFileSync("/dev/stdin").toString().trim().split(" ")

const [N, K] = input.map(x => parseInt(x))
let arr = new Array(N+1).fill(1)
let ans = []

for (let i = 2; i <= N; i++ ) {
    if (arr[i] === 1) {
        arr[i] = 0
        ans.push(i)
        for (let j = i+i; j <= N; j += i) {
            if (arr[j] === 1) {
                arr[j] = 0
                ans.push(j)
            }
        }
    }
}
console.log(ans[K-1])