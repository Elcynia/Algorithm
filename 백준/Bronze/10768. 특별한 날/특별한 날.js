const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n').map(Number);

if (input[0] === 2 && input[1] === 18) console.log('Special');
else if (input[0] < 2 || (input[0] === 2 && input[1] < 18)) console.log('Before');
else console.log('After');
