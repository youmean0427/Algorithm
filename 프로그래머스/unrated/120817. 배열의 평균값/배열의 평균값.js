function solution(numbers) {
    var answer = 0
    for (i in numbers) {
        answer += numbers[i]
    }

    answer /= numbers.length
    
    return answer;
}