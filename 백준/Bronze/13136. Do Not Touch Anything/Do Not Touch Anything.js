const fs = require('fs');
const [r, c, n] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

const a = Math.ceil(r / n);
const b = Math.ceil(c / n);

console.log(a * b);
