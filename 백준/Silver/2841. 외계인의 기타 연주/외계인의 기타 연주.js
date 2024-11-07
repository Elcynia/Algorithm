const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, P] = input[0].split(' ').map(Number);
let fingers = Array(7)
  .fill()
  .map(() => []);
let moves = 0;

for (let i = 1; i <= N; i++) {
  const [line, fret] = input[i].split(' ').map(Number);

  while (fingers[line].length > 0 && fingers[line][fingers[line].length - 1] > fret) {
    fingers[line].pop();
    moves++;
  }

  if (fingers[line].length === 0 || fingers[line][fingers[line].length - 1] < fret) {
    fingers[line].push(fret);
    moves++;
  }
}

console.log(moves);
