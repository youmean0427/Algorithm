function solution(n, words) {
    var answer = [0, 0];

    var arr = [words[0]]
    let i = 1
    let player = 2
    let turn = 1
    while (i < words.length) {
        
        if (player > n) {
            player = player % n
            turn += 1
        }
        
        if (arr.includes(words[i])) {
            answer = [player, turn]
            return answer
        }
        
        let word = arr[arr.length-1]
        
        if (word[word.length-1] === words[i][0]) {
            arr.push(words[i])
        } else {
            answer = [player, turn]
            return answer
        }
        
        i++
        player++
        
    }
    return answer;
}