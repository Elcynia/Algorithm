const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);

for (let i = 1; i <= N; i++) {
  console.log(`Class ${i}`);
  const arr = input[i].split(' ').map(Number);
  const scores = arr.slice(1).sort((a, b) => b - a);

  let largest_gap = 0;
  for (let j = 1; j < scores.length; j++) {
    const gap = scores[j - 1] - scores[j];
    if (gap > largest_gap) largest_gap = gap;
  }

  console.log(`Max ${scores[0]}, Min ${scores[scores.length - 1]}, Largest gap ${largest_gap}`);
}
