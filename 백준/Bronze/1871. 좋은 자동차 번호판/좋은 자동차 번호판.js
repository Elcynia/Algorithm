const input = require('fs').readFileSync(0).toString().trim().split('\n');

const getValue = (s) => s.split('').reduce((sum, c) => sum * 26 + c.charCodeAt() - 65, 0);

input.slice(1).forEach((plate) => {
  const [l, n] = plate.split('-');
  console.log(Math.abs(getValue(l) - n) <= 100 ? 'nice' : 'not nice');
});
