const fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
input = input.toString().split("\n");

const [N, M] = input[0].split(" ").map((x) => parseInt(x));
const arr = input[1].split(" ").map((x) => parseInt(x));
const result = [];

function prime(num) {
  for (let i = 2; i <= parseInt(num ** (1 / 2)); i++) {
    if (num % i == 0) {
      return false;
    }
  }
  return true;
}

function dfs(n, sm) {
  if (sm.length === M) {
    const sum = sm.reduce((a, b) => (a += b), 0);
    if (prime(sum)) {
      result.push(sum);
    }
    return;
  }
  if (n > N - 1) {
    return;
  }

  sm.push(arr[n]);
  dfs(n + 1, sm);
  sm.pop();
  dfs(n + 1, sm);
}

dfs(0, []);
if (result.length) {
  const resultSet = new Set(result);
  const resultList = Array.from(resultSet).sort((a, b) => a - b);
  console.log(resultList.join(" "));
} else {
  console.log(-1);
}
