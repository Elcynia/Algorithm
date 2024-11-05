const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const s = input[0];
const t = input[1];

console.log(s.repeat(t.length) === t.repeat(s.length) ? 1 : 0);
