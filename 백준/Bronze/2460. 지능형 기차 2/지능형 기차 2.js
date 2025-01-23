const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
let stations = input.map((v) => v.split(' ').map(Number));
let cur = 0;
let mx = 0;

for (let [out, on] of stations) {
  cur = cur - out + on;
  mx = Math.max(mx, cur);
}

console.log(mx);