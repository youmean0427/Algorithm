function solution(a, b) {
    const last_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    const day = {1:"FRI", 2:"SAT", 3:"SUN", 4:"MON", 5:"TUE", 6: "WED", 0: "THU"}
    let date = last_day.slice(0, a).reduce((a, b) => a += b) + b
    let answer = day[ date % 7]
    return answer;
}