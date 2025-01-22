const fs = require('fs');
const [n, m, k] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
console.log(k * m + m);
