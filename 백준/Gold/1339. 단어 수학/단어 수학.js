const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();

const weightMap = new Map();

for (let i = 0; i < N; i++) {
  const word = input[i];
  const len = word.length;

  for (let j = 0; j < len; j++) {
    const char = word[j];
    const power = len - j - 1;
    weightMap.set(char, (weightMap.get(char) || 0) + Math.pow(10, power));
  }
}

const sorted = [...weightMap.entries()].sort((a, b) => b[1] - a[1]);

let num = 9;
const charToDigit = new Map();
for (const [char] of sorted) {
  charToDigit.set(char, num--);
}

let total = 0;
for (let word of input) {
  let value = '';
  for (let char of word) {
    value += charToDigit.get(char);
  }
  total += +value;
}

console.log(total);
