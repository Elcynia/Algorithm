const fs = require('fs');
const [month, day] = fs.readFileSync(0).toString().trim().split('\n').map(Number);

const isSpecialDay = month === 2 && day === 18;
const isBeforeSpecialDay = month < 2 || (month === 2 && day < 18);
console.log(isSpecialDay ? 'Special' : isBeforeSpecialDay ? 'Before' : 'After');
