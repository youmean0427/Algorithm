let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input
  .toString()
  .trim()
  .split(" ")
  .map((x) => Number(x));

const N = input[0];
const K = input[1];

dp = new Array(100001).fill(Infinity);
ans = Infinity;

function bfs(n, sec) {
  q = [[n, sec]];
  dp[n] = 0;

  while (q.length) {
    let [x, y] = q.shift();

    if (y > ans) {
      continue;
    }

    if (x === K) {
      ans = Math.min(ans, y);
    }

    if (x + 1 <= 100000) {
      if (dp[x + 1] > y + 1) {
        dp[x + 1] = y + 1;
        q.push([x + 1, y + 1]);
      }
    }

    if (x - 1 >= 0) {
      if (dp[x - 1] > y + 1) {
        dp[x - 1] = y + 1;
        q.push([x - 1, y + 1]);
      }
    }

    if (2 * x >= 0 && 2 * x <= 100000) {
      if (dp[2 * x] > y) {
        dp[2 * x] = y;
        q.push([2 * x, y]);
      }
    }
  }
}

bfs(N, 0);
console.log(ans);
