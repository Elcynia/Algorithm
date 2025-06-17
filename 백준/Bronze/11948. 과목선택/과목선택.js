const fs = require('fs');
const [a, b, c, d, e, f] = fs.readFileSync(0).toString().trim().split('\n').map(Number);
const cal1 = Math.min(a, b, c, d);
const cal2 = Math.min(e, f);
console.log(a + b + c + d + e + f - cal1 - cal2);
