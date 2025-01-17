const fs = require('fs');
const [A, P, C] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

console.log(Math.max(A + C, P));
