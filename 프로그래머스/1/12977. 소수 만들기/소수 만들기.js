function solution(nums) {
    let answer = 0;
    const N = nums.length;
    let primeNums = new Array(3001).fill(0);
    
    // 소수를 찾는 함수
    function prime() {
        for (let i = 2; i < 3001; i++) {
            let ii = i + i;
            while (ii < 3001) {
                primeNums[ii] = 1;
                ii += i;
            }
        }
    }
    prime();
    
    // DFS 함수
    function dfs(idx, count, sum) {
        if (count === 3) { // 세 개의 수를 더한 경우
            if (primeNums[sum] === 0) { // 소수인지 확인
                answer += 1;
            }
            return;
        }
        
        for (let i = idx; i < N; i++) {
            dfs(i + 1, count + 1, sum + nums[i]); // 다음 숫자로 이동
        }
    }
    
    dfs(0, 0, 0); // DFS 시작
    
    return answer;
}
