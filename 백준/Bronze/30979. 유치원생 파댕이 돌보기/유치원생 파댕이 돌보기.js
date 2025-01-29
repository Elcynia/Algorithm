const fs = require('fs');
const [T, , F] = fs.readFileSync(0).toString().trim().split('\n');

console.log(F.split(' ').reduce((sum, time) => sum + +time, 0) >= +T ? 'Padaeng_i Happy' : 'Padaeng_i Cry');
