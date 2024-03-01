let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input.toString().trim().split("\n");
input.sort();

const N = parseInt(input[0]);
let cnt = {};
for (let i = 1; i <= N; i++) {
  first = input[i][0];
  if (first in cnt) {
    cnt[first] += 1;
  } else {
    cnt[first] = 1;
  }
}

answer = "";
for (let i in cnt) {
  if (cnt[i] >= 5) {
    answer += i;
  }
}

if (answer === "") {
  console.log("PREDAJA");
} else {
  console.log(answer);
}
