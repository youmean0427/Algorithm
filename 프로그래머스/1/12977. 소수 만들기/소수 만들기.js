function solution(nums) {
    var answer = 0
    const N = nums.length
    let primeNums = new Array(3001).fill(0)
    
    function prime() {
        for (let i = 2; i < 3001; i++) {
            let ii = i + i
            while (ii < 3001) {
                primeNums[ii] = 1
                ii += i
            }
        }
    }
    prime()
    
    for (let a = 0; a < N; a++) {
        for (let b = a+1; b < N; b++) {
            for (let c = b+1; c < N; c++) {
                let addNum = nums[a]+nums[b]+nums[c]
                if (primeNums[addNum] == 0) {
                    answer += 1
                }
            }
        }
    }
    
    return answer;
}