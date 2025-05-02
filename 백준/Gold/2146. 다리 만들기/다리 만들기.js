const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const land = input.map((v) => v.split(' ').map(Number));
const dy = [0, 0, -1, 1];
const dx = [-1, 1, 0, 0];

function markIslands() {
  let cnt = 1;
  const visited = Array.from({ length: N }, () => Array(N).fill(0));

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (land[i][j] === 1 && !visited[i][j]) {
        const Q = [[i, j]];
        visited[i][j] = 1;
        land[i][j] = cnt;

        while (Q.length) {
          const [cy, cx] = Q.shift();
          for (let d = 0; d < 4; d++) {
            const ny = cy + dy[d];
            const nx = cx + dx[d];

            if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;
            if (land[ny][nx] === 1 && !visited[ny][nx]) {
              visited[ny][nx] = 1;
              land[ny][nx] = cnt;
              Q.push([ny, nx]);
            }
          }
        }
        cnt++;
      }
    }
  }
  return cnt - 1; // 섬의 개수
}

// 최단 다리 길이
function BridgeLength(islandNum) {
  const dist = Array.from({ length: N }, () => Array(N).fill(-1));
  const Q = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (land[i][j] === islandNum) {
        // 바다 체크
        let isCoast = false;
        for (let k = 0; k < 4; k++) {
          const ny = i + dy[k];
          const nx = j + dx[k];
          if (ny > 0 && nx > 0 && ny < N && nx < N && land[ny][nx] === 0) {
            isCoast = true;
            break;
          }
        }

        if (isCoast) {
          Q.push([i, j]);
          dist[i][j] = 0;
        }
      }
    }
  }

  // 다른 섬까지 거리
  while (Q.length) {
    const [cy, cx] = Q.shift();
    for (let i = 0; i < 4; i++) {
      const ny = cy + dy[i];
      const nx = cx + dx[i];

      if (ny < 0 || nx < 0 || ny >= N || nx >= N) continue;

      // 아직 방문하지 않은 바다인 경우
      if (land[ny][nx] === 0 && dist[ny][nx] === -1) {
        dist[ny][nx] = dist[cy][cx] + 1;
        Q.push([ny, nx]);
      }

      // 다른 섬에 도달한 경우
      else if (land[ny][nx] !== 0 && land[ny][nx] !== islandNum) {
        return dist[cy][cx]; // 현재 칸까지의 거리가 다리의 길이
      }
    }
  }

  return Infinity; // 다른 섬에 도달할 수 없는 경우
}

const landCnt = markIslands();
let minBridgeLength = Infinity;

// 각 섬에서 시작하여 다른 섬까지의 최단 다리 길이 계산
for (let i = 1; i <= landCnt; i++) {
  const bridgeLength = BridgeLength(i);
  minBridgeLength = Math.min(minBridgeLength, bridgeLength);
}

console.log(minBridgeLength);
