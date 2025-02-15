const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [R, C] = input[0].split(' ').map(Number);
const map = input.slice(1);

const result = new Array(5).fill(0);

function checkParkingSpace(row, col) {
  if (row + 1 >= R || col + 1 >= C) return -1;

  let cars = 0;
  for (let i = row; i < row + 2; i++) {
    for (let j = col; j < col + 2; j++) {
      if (map[i][j] === '#') return -1;
      if (map[i][j] === 'X') cars++;
    }
  }
  return cars;
}

for (let i = 0; i < R; i++) {
  for (let j = 0; j < C; j++) {
    const cars = checkParkingSpace(i, j);
    if (cars !== -1) {
      result[cars]++;
    }
  }
}

console.log(result.join('\n'));
