const fs = require('fs');
const n = +fs.readFileSync(0).toString() - 1;

// 0xAC00 ('가'의 코드값)
console.log(String.fromCharCode(0xac00 + Math.floor(n / 28) * 28 + (n % 28)));
