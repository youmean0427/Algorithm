function solution(num_list) {
    var answer = [];
    let even = 0
    let odd = 0
    
    for (let i = 0; i < num_list.length; i++ ) {
        (num_list[i] % 2 == 0) ? even += 1 : odd += 1 
    }
    answer = [even, odd]
    return answer;
}