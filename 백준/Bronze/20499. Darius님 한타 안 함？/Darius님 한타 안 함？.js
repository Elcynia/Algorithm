const fs = require('fs');
const [K, D, A] = fs.readFileSync(0).toString().trim().split('/').map(Number);
console.log(K + A < D || (K === 0 && D === 0) ? 'hasu' : 'gosu');