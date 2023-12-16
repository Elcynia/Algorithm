#include <bits/stdc++.h>
using namespace std;
#define setio              \
  ios::sync_with_stdio(0); \
  cin.tie(0);
#define endl "\n";
/*
1: 익토 (익은 토마토)
0: 안익토 (안 익은 토마토)
-1: 빈토 (들어있지 않은 토마토)
*/

int n, m, h;
int board[102][102][102];
int dist[102][102][102];
// 하-우-상-좌-전-후
int dx[6] = {1, 0, -1, 0, 0, 0};
int dy[6] = {0, 1, 0, -1, 0, 0};
int dz[6] = {0, 0, 0, 0, 1, -1};
queue<tuple<int, int, int>> Q;

void bfs() {
  while (!Q.empty()) {
    int curX, curY, curZ;
    tie(curZ, curY, curX) = Q.front();
    Q.pop();

    for (int i = 0; i < 6; i++) {
      int nx = curX + dx[i];
      int ny = curY + dy[i];
      int nz = curZ + dz[i];

      if (nx < 0 || ny < 0 || nz < 0 || nx >= m || ny >= n || nz >= h) continue;
      if (dist[nz][ny][nx] >= 0) continue;

      dist[nz][ny][nx] = dist[curZ][curY][curX] + 1;
      Q.push({nz, ny, nx});
    }
  }
}
int main(void) {
  setio;
  cin >> m >> n >> h;
  for (int k = 0; k < h; k++) {      // 층(height)
    for (int i = 0; i < n; i++) {    // 행(row)
      for (int j = 0; j < m; j++) {  // 열(column)
        cin >> board[k][i][j];
        if (board[k][i][j] == 1) Q.push({k, i, j});  // 익토(1)는 Queue에 저장
        if (board[k][i][j] == 0)
          dist[k][i][j] = -1;  // 안익토(0)는 dist 배열에 -1로 저장
      }
    }
  }
  bfs();
  int max_day = 0;
  for (int k = 0; k < h; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (dist[k][i][j] == -1) {
          cout << -1 << endl;
          return 0;
        }
        max_day = max(max_day, dist[k][i][j]);
      }
    }
  }
  cout << max_day << endl;
  return 0;
}