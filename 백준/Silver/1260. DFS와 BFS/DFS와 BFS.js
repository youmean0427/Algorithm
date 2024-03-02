let fs = require("fs");
let input = fs.readFileSync("/dev/stdin");
// let input = fs.readFileSync("./input.txt");
input = input.toString().trim().split("\n");

const [N, M, V] = input[0].split(" ").map((x) => parseInt(x));
let arr = Array.from({ length: N + 1 }, () => []);

for (let i = 1; i <= M; i++) {
  const [a, b] = input[i].split(" ").map((x) => parseInt(x));
  arr[a].push(b);
  arr[b].push(a);
}

function DFS(start) {
  let stack = [start];
  visited = new Array(N + 1).fill(0);
  ans = [];
  while (stack.length) {
    x = stack.pop();
    if (visited[x] === 0) {
      ans.push(x);
      visited[x] = 1;
      arr[x] = arr[x].sort((a, b) => b - a);
      for (let i = 0; i < arr[x].length; i++) {
        if (visited[arr[x][i]] === 0) {
          stack.push(arr[x][i]);
        }
      }
    }
  }
  return ans;
}

function BFS(start) {
  let queue = [start];
  visited = new Array(N + 1).fill(0);
  visited[start] = 1;
  ans = [];
  while (queue.length) {
    x = queue.shift();
    ans.push(x);
    arr[x] = arr[x].sort((a, b) => a - b);
    for (let i = 0; i < arr[x].length; i++) {
      if (visited[arr[x][i]] === 0) {
        visited[arr[x][i]] = 1;
        queue.push(arr[x][i]);
      }
    }
  }
  return ans;
}

const dfs = DFS(V);
const bfs = BFS(V);
console.log(...dfs);
console.log(...bfs);
