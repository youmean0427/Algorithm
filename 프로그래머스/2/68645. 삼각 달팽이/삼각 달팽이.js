function solution(n) {
    var answer = [];
    let arr = Array.from({length : n}, () => new Array(n).fill(0))
    let  exit = 0
    for (let i = 1; i <= n; i++) {
        exit += i
    }
    
    function dfs(sn, sm) {
        
        arr[sn][sm] = 1
        let stack = [[sn, sm]]
        let dir_idx = 0
        const dir = [[1, 0], [0, 1], [-1, -1]]
        const dir_chan = {0 : 1, 1: 2, 2: 0}
        
        while (stack.length) {
            const [x, y] = stack.pop()
            const [dn, dm] = dir[dir_idx]
            
            if (arr[x][y] === exit) {
                return 
            }
            
            const xn = x + dn
            const ym = y + dm
            
            if ( 0 <= xn && xn < n && 0<= ym && ym < n) {
                if (arr[xn][ym] === 0) {
                arr[xn][ym] = arr[x][y] + 1
                stack.push([xn, ym])
                continue
                }
            }
            dir_idx = dir_chan[dir_idx]
            stack.push([x, y])
        }
    }
    dfs(0, 0)
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (arr[i][j] > 0) {
                answer.push(arr[i][j])
            }
        }
    }
    return answer;
}