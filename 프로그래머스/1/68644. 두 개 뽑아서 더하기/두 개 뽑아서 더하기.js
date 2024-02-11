function solution(numbers) {

    let sum = [];
    let ans = []
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            sum.push(numbers[i] + numbers[j])
        }
    }
    
    ans = [...new Set(sum)]
    ans.sort((a, b) => a - b)
    
    return ans
}