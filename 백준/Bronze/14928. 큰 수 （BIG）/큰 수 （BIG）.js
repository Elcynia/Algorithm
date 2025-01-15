const fs = require('fs');
const N = fs.readFileSync(0).toString().trim();

let result = 0;
for (let i = 0; i < N.length; i++) {
  result = (result * 10 + +N[i]) % 20000303;
}

console.log(result);
