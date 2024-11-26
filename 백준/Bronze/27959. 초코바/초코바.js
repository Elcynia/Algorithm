const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(' ');
const N = +input[0];
const M = +input[1];
const totalMoney = 100 * N;
console.log (totalMoney >= M ? "Yes" : "No");