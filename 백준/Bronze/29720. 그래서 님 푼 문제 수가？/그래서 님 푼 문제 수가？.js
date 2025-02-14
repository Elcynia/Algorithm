const fs = require('fs');
const [N, M, K] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
console.log(Math.max(N - M * K, 0), N - M * (K - 1) - 1);
