function solution(numbers) {
    var answer = 0
    arr = [1, 2, 3, 4,5, 6, 7, 8, 9, 0]
    for (const i of arr) {
          if (!numbers.includes(i)) {
              answer += i
          }
    }

    return answer;
}