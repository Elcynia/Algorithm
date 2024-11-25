const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [R, C] = input[0].split(' ').map(Number);
const arr = input.slice(1);
const positions = Array(10).fill(0);

for (let i = 0; i < R; i++) {
  for (let j = C - 2; j >= 0; j--) {
    if (arr[i][j] !== '.' && arr[i][j] !== 'S' && arr[i][j] !== 'F') {
      const teamNum = parseInt(arr[i][j]);
      positions[teamNum] = C - 2 - j;
      break;
    }
  }
}

const distances = [...new Set(positions.slice(1))].sort((a, b) => a - b);
const ranks = {};
distances.forEach((dist, idx) => {
  ranks[dist] = idx + 1;
});

for (let i = 1; i <= 9; i++) {
  console.log(ranks[positions[i]]);
}
