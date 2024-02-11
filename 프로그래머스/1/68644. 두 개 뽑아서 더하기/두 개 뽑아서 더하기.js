function solution(numbers) {

    
    let answer = [];
    let ans = []
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i+1; j < numbers.length; j++) {
            answer.push([numbers[i], numbers[j]])
        }
    }
    
    answer.forEach(x => {
        let res = x.reduce((a, b) => a += b)
        if (!ans.includes(res)) {
            ans.push(res)
        }
    })
    
    ans.sort((a, b) => a - b)
    return ans;
}