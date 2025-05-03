const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [R, C] = input.shift().split(' ').map(Number);
const board = input.map((v) => v.split(''));
const dy = [0, 0, -1, 1];
const dx = [-1, 1, 0, 0];
const waterTime = Array.from({ length: R }, () => Array(C).fill(-1));
const animalTime = Array.from({ length: R }, () => Array(C).fill(-1));

const water = [];
const animal = [];
let start, end;

for (let i = 0; i < R; i++) {
  for (let j = 0; j < C; j++) {
    if (board[i][j] === 'S') {
      start = [i, j];
      animalTime[i][j] = 0;
      animal.push([i, j]);
    } else if (board[i][j] === 'D') {
      end = [i, j];
    } else if (board[i][j] === '*') {
      waterTime[i][j] = 0;
      water.push([i, j]);
    }
  }
}

// 물
while (water.length) {
  const [y, x] = water.shift();
  for (let d = 0; d < 4; d++) {
    const ny = y + dy[d];
    const nx = x + dx[d];
    if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;
    if (board[ny][nx] !== '.' && board[ny][nx] !== 'S') continue;
    if (waterTime[ny][nx] !== -1) continue;
    waterTime[ny][nx] = waterTime[y][x] + 1;
    water.push([ny, nx]);
  }
}

// 고슴도치
while (animal.length) {
  const [y, x] = animal.shift();
  for (let d = 0; d < 4; d++) {
    const ny = y + dy[d];
    const nx = x + dx[d];
    if (ny < 0 || nx < 0 || ny >= R || nx >= C) continue;

    if (board[ny][nx] !== '.' && board[ny][nx] !== 'D') continue;
    if (animalTime[ny][nx] !== -1) continue;

    const nextTime = animalTime[y][x] + 1;

    // 물이 이미 있고, 나보다 먼저 or 동시에 도착이면 못 감
    if (waterTime[ny][nx] !== -1 && waterTime[ny][nx] <= nextTime) continue;

    animalTime[ny][nx] = nextTime;
    animal.push([ny, nx]);
  }
}

const [ey, ex] = end;
console.log(animalTime[ey][ex] === -1 ? 'KAKTUS' : animalTime[ey][ex]);
