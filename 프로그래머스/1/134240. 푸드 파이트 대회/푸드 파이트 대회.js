function solution(food) {
    var answer = [];
    
    for (let i = 0; i < food.length; i++) {
        food[i] = Math.floor(food[i] / 2)
        while (food[i]) {
            answer.push(i)
            food[i] -= 1
        }
    }
    answer = answer.join("") + '0' + answer.reverse().join("")
    
    
    return answer;
}