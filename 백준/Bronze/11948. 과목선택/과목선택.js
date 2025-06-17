const [a, b, c, d, e, f] = require('fs').readFileSync(0).toString().trim().split('\n').map(Number);
console.log(a + b + c + d + e + f - Math.min(a, b, c, d) - Math.min(e, f));
