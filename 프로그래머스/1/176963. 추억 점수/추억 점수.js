function solution(name, yearning, photo) {
    var answer = [];
    let obj = {};
    
    for (let i = 0; i < name.length; i++) {
        obj[name[i]] = yearning[i]
    }
    
    for (let j = 0; j < photo.length; j++) {
        let score = 0
        for (const k of photo[j]) {
            if (k in obj) {
                score += obj[k]
            }
        }
        answer.push(score)
    }
    
    return answer;
}