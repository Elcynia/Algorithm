const fs = require('fs');
const n = +fs.readFileSync(0).toString().trim();

r = 0;
function fibonacci(n) {
  if (n === 0) return 0;
  if (n === 1) return 1;
  r += n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(n));
