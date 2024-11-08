const fs = require('fs');
let [n, m, k] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
n = Math.floor(k / m);
m = k % m;
console.log(n, m);
