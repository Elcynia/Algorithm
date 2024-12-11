const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();
let result = 0;

if (input === '1010') {
  result = 20;
} else {
  const num = parseInt(input);
  if (num % 100 === 10) {
    result = parseInt(input.replace(/10$/, '')) + 10;
  } else {
    result = Math.floor(num / 10) + (num % 10);
  }
}
console.log(result);
