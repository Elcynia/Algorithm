const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [h, m, s] = input[0].split(' ').map(Number);
const seconds = +input[1];

let totalSeconds = h * 3600 + m * 60 + s;

totalSeconds += seconds;

totalSeconds %= 86400;

const endHour = Math.floor(totalSeconds / 3600);
const endMin = Math.floor((totalSeconds % 3600) / 60);
const endSec = totalSeconds % 60;

console.log(endHour, endMin, endSec);
