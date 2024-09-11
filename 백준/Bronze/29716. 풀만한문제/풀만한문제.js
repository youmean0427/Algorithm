const fs = require("fs");
const input = fs.readFileSync(0).toString().trim().split("\n");

const [J, N] = input[0].split(" ").map((x) => Number(x));
let ans = 0;

for (let i = 1; i <= N; i++) {
    let total = 0;

    for (let j = 0; j <= input[i].length - 1; j++) {
        if (input[i][j] >= "A" && input[i][j] <= "Z") total += 4;
        else if (input[i][j] == " ") total += 1;
        else if (
            (input[i][j] >= "a" && input[i][j] <= "z") ||
            (input[i][j] >= "0" && input[i][j] <= "9")
        )
            total += 2;
    }
    if (total <= J) ans++;
}

console.log(ans);
