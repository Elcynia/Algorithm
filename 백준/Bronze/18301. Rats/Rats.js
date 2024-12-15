const fs = require('fs');
const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

console.log(Math.trunc(((a + 1) * (b + 1)) / (c + 1) - 1));
