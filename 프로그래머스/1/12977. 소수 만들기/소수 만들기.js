function solution(nums) {
    var answer = 0
    const N = nums.length
    
    function prime(n) {
        for (let i = 2; i <= n ** (1/2); i++) {
            if (n % i == 0) {
                return false
            }
        }
        return true
    }
    
    for (let a = 0; a < N; a++) {
        for (let b = a+1; b < N; b++) {
            for (let c = b+1; c < N; c++) {
                let addNum = nums[a]+nums[b]+nums[c]
                if (prime(addNum)) {
                    answer += 1
                }
            }
        }
    }
    
    return answer;
}