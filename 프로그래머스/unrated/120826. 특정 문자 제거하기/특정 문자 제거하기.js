function solution(my_string, letter) {
    var answer = '';
    for (i of my_string) {
        if (i != letter) {
            answer += i
        }
    }
    
    return answer;
}