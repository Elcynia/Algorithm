const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
console.log(input.toLowerCase() === 'n' ? 'Naver D2' : 'Naver Whale');
