const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = +input[0];
const arr = input.slice(1).map(Number);
let cnt = 0;
for (let i = 0; i < n; i++) {
    if (arr[i] % 2 !== 0) {
        cnt++;
    }
}
console.log(cnt);