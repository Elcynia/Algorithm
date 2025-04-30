const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, L, R] = input.shift().split(' ').map(Number);
const populations = input.map((v) => v.split(' ').map(Number));
const dy = [0, 0, -1, 1];
const dx = [-1, 1, 0, 0];

function BFS(y, x, visited) {
  const Q = [[y, x]];
  const union = [[y, x]]; // 연합 소속 좌표
  visited[y][x] = true;
  let totalPopulation = populations[y][x]; // 연합의 총 인구수, 50

  while (Q.length) {
    const [y, x] = Q.shift();

    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];

      if (ny < 0 || nx < 0 || ny >= N || nx >= N || visited[ny][nx]) continue;

      const diff = Math.abs(populations[y][x] - populations[ny][nx]); // 20
      if (diff >= L && diff <= R) {
        Q.push([ny, nx]); // 0, 1
        union.push([ny, nx]); // 0, 1
        visited[ny][nx] = true;
        totalPopulation += populations[ny][nx];
      }
    }
  }

  // 연합이 형성되었다면 인구 이동 발생
  if (union.length > 1) {
    const newPopulation = Math.floor(totalPopulation / union.length);
    for (const [uy, ux] of union) {
      populations[uy][ux] = newPopulation;
    }
    return true; // 인구 이동 발생
  }

  return false; // 인구 이동 없음
}

let day = 0;

while (true) {
  const visited = Array.from(Array(N), () => Array(N).fill(false));
  let isMoved = false;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!visited[i][j]) {
        if (BFS(i, j, visited)) {
          isMoved = true;
        }
      }
    }
  }

  // 더 이상 인구 이동이 없으면 종료
  if (!isMoved) break;
  day++;
}

console.log(day);
