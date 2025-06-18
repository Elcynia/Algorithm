const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [A, B] = input[0].split(' ').map(Number);
const [C, D] = input[1].split(' ').map(Number);

const answer = Math.min(A + D, B + C);
console.log(answer);
