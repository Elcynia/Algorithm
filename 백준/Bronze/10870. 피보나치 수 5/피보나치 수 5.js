const fs = require('fs');
const n = +fs.readFileSync(0).toString().trim();
let arr = new Array(n + 2).fill(-1);
arr[0] = 0;
arr[1] = 1;
function fibonacci(n) {
  if (arr[n] !== -1) return arr[n];
  arr[n] = fibonacci(n - 1) + fibonacci(n - 2);
  return fibonacci(n);
}
console.log(fibonacci(n));