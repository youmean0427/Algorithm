let fs = require('fs');
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let q = [];
let result = "";

let front = 0;
let back = 0;

for (let i = 1; i < parseInt(input[0]) + 1; i++) {
    let line = input[i].split(" ");
    let word = line[0].trim();

    if (word === "push") {
        q[back++] = parseInt(line[1]);
        continue;
    }
    if (word === 'pop') {
        if (front < back) {
            const x = q[front++];
            result += x + '\n';
        } else {
            result += "-1\n";
        }
        continue;
    }
    if (word === 'size') {
        result += back - front + "\n";
        continue;
    }
    if (word === 'empty') {
        if (front < back) {
            result += "0\n";
        } else {
            result += "1\n";
        }
        continue;
    }
    if (word === 'front') {
        if (front < back) {
            result += q[front] + "\n";
        } else {
            result += "-1\n";
        }
        continue;
    }
    if (word === 'back') {
        if (front < back) {
            result += q[back - 1] + "\n";
        } else {
            result += "-1\n";
        }
        continue;
    }
}

console.log(result);