const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [n, k] = input[0].split(' ').map(Number);

const isDescending = (arr) => arr.every((v, i) => i === 0 || v <= arr[i - 1]);

for (let i = 2; i < input.length; i += 2) {
  if (!isDescending(input[i].split(' ').map(Number))) {
    console.log('No');
    return;
  }
}

console.log('Yes');
