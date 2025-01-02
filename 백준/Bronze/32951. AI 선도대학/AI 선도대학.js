const fs = require('fs');
const N = +fs.readFileSync(0).toString().trim();
console.log(N - 2024);
