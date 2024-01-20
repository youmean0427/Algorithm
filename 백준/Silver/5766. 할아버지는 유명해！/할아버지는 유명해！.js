let fs = require('fs')
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n')
// let input = fs.readFileSync('./EX.txt').toString().trim().split("\n")

idx = 0
while (idx !== input.length-1) {
    const[N, M] = input[idx].split(" ").map(x => parseInt(x))
    
    cnt = {}
    for(let i = idx+1; i < idx + N+1; i++) {
        arr = input[i].split(" ").map(x => parseInt(x))
        arr.forEach(x => {if (x in cnt) {
            cnt[x] += 1
        } else {cnt[x] = 1}})
    }

    cntSort = Object.entries(cnt)
    cntSort.sort((a, b) => b[1] - a[1] || a[0] - b[0])

    answer = ""
    first = cntSort[0][1]
    second = 0
    cntSort.forEach(x => {if (x[1] !== first && x[1] >= second) { 
        second = x[1] 
        answer += x[0] + " "
    }})

    console.log(answer)
    idx += N+1
}
