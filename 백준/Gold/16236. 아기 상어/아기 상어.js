const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input.shift();
const dy = [-1, 0, 0, 1];
const dx = [0, -1, 1, 0];
let time = 0;
let babyShark = 2;
let eat = 0;
const board = input.map((v) => v.split(' ').map(Number));
let sharkY, sharkX;

// 아기 상어의 초기 위치 찾기
for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    if (board[i][j] === 9) {
      sharkY = i;
      sharkX = j;
      board[i][j] = 0; // 상어가 있던 자리는 빈 칸으로 변경
    }
  }
}

function BFS() {
  const visited = Array.from(Array(N), () => Array(N).fill(false));
  const Q = [[sharkY, sharkX, 0]]; // [y, x, 이동 거리]
  visited[sharkY][sharkX] = 1;

  const fishes = []; // 물고기

  while (Q.length) {
    const [y, x, dist] = Q.shift();

    // 현재 위치에 물고기가 있고, 아기 상어보다 작으면 먹을 수 있음
    if (board[y][x] > 0 && board[y][x] < babyShark) {
      fishes.push([y, x, dist]);
    }

    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];
      if (ny < 0 || nx < 0 || ny >= N || nx >= N || visited[ny][nx]) continue;

      // 아기 상어보다 큰 물고기가 있는 칸은 패스
      if (board[ny][nx] > babyShark) continue;
      visited[ny][nx] = 1;
      Q.push([ny, nx, dist + 1]);
    }
  }

  // 먹을 수 있는 물고기가 없다면 return
  if (fishes.length === 0) return;

  // 거리순 -> 위쪽 -> 왼쪽 순으로 정렬
  fishes.sort((a, b) => {
    if (a[2] !== b[2]) return a[2] - b[2]; // 거리 우선
    if (a[0] !== b[0]) return a[0] - b[0]; // 위쪽 우선
    return a[1] - b[1]; // 왼쪽 우선
  });

  return fishes[0]; // 가장 우선순위가 높은 물고기 반환
}

while (true) {
  const bfs = BFS();

  // 더 이상 먹을 수 있는 물고기가 없으면 종료
  if (!bfs) break;

  const [fishY, fishX, distance] = bfs;

  // 물고기 섭취
  board[fishY][fishX] = 0;
  time += distance;

  // 아기 상어 위치 업데이트
  sharkY = fishY;
  sharkX = fishX;

  // 먹은 물고기 수 증가 및 성장 조건 확인
  eat++;
  if (eat === babyShark) {
    babyShark++; // 아기 상어 크기 증가
    eat = 0; // 먹은 물고기 수 초기화
  }
}

console.log(time);
