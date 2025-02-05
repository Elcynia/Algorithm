const fs = require('fs');
const [a, b, c] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

if (a === 0) {
  console.log(c ** 2 - b);
} else if (b === 0) {
  console.log(c ** 2 - a);
} else {
  console.log(Math.sqrt(a + b));
}
