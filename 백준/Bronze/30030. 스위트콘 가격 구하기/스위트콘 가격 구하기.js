const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
const B = parseInt(input);
const A = Math.floor((B * 100) / 110);
console.log(A);
