const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [M, N] = input.shift().split(' ').map(Number);
const arr = input.map((v) => v.split(' ').map(Number));
const dp = Array.from({ length: M }, () => Array(N).fill(-1));
const dy = [0, 0, 1, -1];
const dx = [1, -1, 0, 0];

function dfs(y, x) {
  // 도착
  if (y === M - 1 && x === N - 1) {
    return 1;
  }

  // 이미 방문했으면 해당 값 반환
  if (dp[y][x] !== -1) {
    return dp[y][x];
  }

  let cnt = 0;
  for (let i = 0; i < 4; i++) {
    const ny = y + dy[i];
    const nx = x + dx[i];
    if (ny < 0 || nx < 0 || ny >= M || nx >= N) continue;

    // 내리막길인 경우
    if (arr[y][x] > arr[ny][nx]) {
      cnt += dfs(ny, nx);
    }
  }

  return (dp[y][x] = cnt);
}

console.log(dfs(0, 0));
