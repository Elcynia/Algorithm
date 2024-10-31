const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

for (let i = 0; i < input.length; i++) {
  const [M, F] = input[i].split(' ').map(Number);
  if (M === 0 && F === 0) break;
  console.log(M + F);
}
