const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const arr = input.slice(1).map((line) => line.split(' '));
const N = input[0];
let ans = 0;

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const permutations = [];

for (let i = 0; i < numbers.length; i++) {
  for (let j = 0; j < numbers.length; j++) {
    if (j === i) continue;
    for (let k = 0; k < numbers.length; k++) {
      if (k === i || k === j) continue;
      permutations.push([numbers[i], numbers[j], numbers[k]]);
    }
  }
}

for (const perm of permutations) {
  let isAnswer = true;

  for (const [num, strike, ball] of arr) {
    let strikes = 0;
    let balls = 0;
    for (let i = 0; i < 3; i++) {
      if (perm[i] === parseInt(num[i])) {
        strikes++;
      } else if (num.includes(perm[i].toString())) {
        balls++;
      }
    }

    if (strikes !== parseInt(strike) || balls !== parseInt(ball)) {
      isAnswer = false;
      break;
    }
  }

  if (isAnswer) ans++;
}

console.log(ans);
