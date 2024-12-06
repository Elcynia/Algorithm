const fs = require('fs');
const [A, B] = fs.readFileSync(0).toString().trim().split(' ').map(BigInt);
console.log((A * B).toString());
