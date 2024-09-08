const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");

const [N, M] = input[0].split(" ").map((x) => Number(x));

const arr = input[1].split(" ").map((x) => Number(x));
arr.sort((a, b) => a - b);

const s_arr = [];

for (let i = 0; i < N; i++) {
    if (s_arr.includes(arr[i])) continue;
    else s_arr.push(arr[i]);
}

const result = [];

function back(cnt, sm) {
    if (cnt === M) {
        result.push(sm.join(" "));
        return;
    }

    for (let i = 0; i < N; i++) {
        if ((sm.length && sm[sm.length - 1] <= s_arr[i]) || sm.length == 0) {
            sm.push(s_arr[i]);
            back(cnt + 1, sm);
            sm.pop();
        }
    }
}

back(0, []);
console.log(result.join("\n"));
