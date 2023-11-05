function solution(s) {
    var answer = '';
    if (s.length % 2 == 0) {
        answer = s.slice(parseInt(s.length / 2)-1, parseInt(s.length / 2)+1)
    } else {
        answer = s[parseInt(s.length / 2)] 
    }
    
    return answer;
}