const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const T = Number(input[0]);
const numbers = new Array(15).fill('');

numbers[0] = '{}';
numbers[1] = '{{}}';

for (let i = 2; i < 16; i++) {
  numbers[i] = numbers[i - 1].slice(0, -1) + ',' + numbers[i - 1] + '}';
}

for (let i = 1; i <= T * 2; i += 2) {
  const A = input[i].trim();
  const B = input[i + 1].trim();

  const result = numbers.indexOf(A) + numbers.indexOf(B);
  console.log(numbers[result]);
}
