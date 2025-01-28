const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [L, P] = input[0].split(' ').map(Number);

const res = input[1].split(' ').map((num) => +num - L * P);
console.log(res.join(' '));
