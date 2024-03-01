let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt")
input = input.toString().trim().split("\n");

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

const name = [];
const keys = Object.keys(cnt);
keys.forEach((key) => {
  if (cnt[key] >= 5) {
    name.push(key);
  }
});

answer = "";
name.sort();
if (name.length) {
  name.forEach((x) => {
    answer += x;
  });
} else {
  answer = "PREDAJA";
}

console.log(answer);