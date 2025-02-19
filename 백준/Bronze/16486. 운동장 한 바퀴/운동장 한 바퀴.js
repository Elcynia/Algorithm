const fs = require('fs');
const [d1, d2] = fs.readFileSync(0).toString().trim().split('\n').map(Number);
console.log(d1 * 2 + 2 * 3.141592 * d2);
