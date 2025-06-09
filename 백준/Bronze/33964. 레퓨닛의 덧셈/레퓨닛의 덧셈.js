const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ').map(Number);
const [x, y] = input;
const result = [];

console.log(+'1'.repeat(x) + +'1'.repeat(y));
