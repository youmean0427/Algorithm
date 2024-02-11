function solution(numbers) {

    
    let answer = [];
    let ans = []
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            answer.push(numbers[i] + numbers[j])
        }
    }
    
    ans = [...new Set(answer)]
    ans.sort((a, b) => a - b)
    
    return ans
}