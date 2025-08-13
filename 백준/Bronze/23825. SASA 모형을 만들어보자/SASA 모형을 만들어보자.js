const fs = require('fs');
const [N, M] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
console.log(Math.floor(Math.min(N / 2, M / 2)));
