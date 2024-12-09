const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
let idx = 0;

function getCombinations(arr, selectNumber) {
  const results = [];

  if (selectNumber === 1) {
    return arr.map((value) => [value]);
  }

  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });

  return results;
}

while (true) {
  const numbers = input[idx].split(' ').map(Number);
  const k = numbers[0];
  if (k === 0) break;
  const S = numbers.slice(1);
  const combinations = getCombinations(S, 6);

  combinations.forEach((combination) => {
    console.log(combination.join(' '));
  });
  console.log();
  idx++;
}
