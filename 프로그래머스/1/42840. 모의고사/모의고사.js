function solution(answers) { 
    var answer = [0, 0, 0];
    let one = [1, 2, 3, 4, 5];
    let two = [2, 1, 2, 3, 2, 4, 2, 5];
    let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    const ol = one.length;
    const tl = two.length;
    const thl = three.length;

    const N = answers.length;

    let i = 0;
    while (i < N) {
        if (answers[i] === one[i%ol]) {
            answer[0] += 1;
        }
        if (answers[i] === two[i%tl]) {
            answer[1] += 1;
        }
        if (answers[i] === three[i%thl]) {
            answer[2] += 1;
        }
        i += 1;
    }
    
    const max_val = Math.max(...answer);
    var result = [];
    for (let j = 0; j < answer.length; j++) {
        if (answer[j] === max_val) {
            result.push(j + 1);
        }
    }
    return result;
}

// 처음에 찍는 방식이 반복되는 것을 생각 못함