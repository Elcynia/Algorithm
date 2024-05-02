#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

/*
익은 토마토: 1,
익지 않은 토마토: 0,
토마토 없는 칸: -1
*/

// 전역변수로 선언된 변수는 따로 초기화를 안 할 시, 0으로 채워짐
// 즉, 익은 토마토 & 빈 칸은 dist가 0으로 채워짐
int m, n;
int board[1002][1002];      // 격자판 ( M*N )
int dist[1002][1002];       // 거리 구하는 용도
int dx[4] = {1, 0, -1, 0};  // x좌표
int dy[4] = {0, 1, 0, -1};  // y좌표

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int ans = 0;
  cin >> n >> m;
  queue<pair<int, int> > Q;

  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      cin >> board[i][j];  // 격자판에 2차원 배열을 입력받는데
      if (board[i][j] == 1) Q.push({i, j});  // 토마토가 익은 상태면(1) Q에 저장
      if (board[i][j] == 0) dist[i][j] = -1;  // 익지 않았으면(0) dist에 -1 저장
    }
  }
  while (!Q.empty()) {  // Q가 빌 때까지 돔
    auto cur = Q.front();
    // cout << cur.first << "," << cur.second << endl;
    // cout << "(" << cur.first << ", " << cur.second << ")" << endl;
    Q.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.first + dx[i];
      int ny = cur.second + dy[i];
      // cout << "[" << nx << "," << ny << "]" << endl;
      if (nx < 0 || ny < 0 || nx >= m || ny >= n)
        continue;                       // 범위 벗어나면 패스
      if (dist[nx][ny] >= 0) continue;  //  0이상이면 패스하고
      dist[nx][ny] = dist[cur.first][cur.second] + 1;  // 문제 특성상, +1
      // cout << dist[nx][ny] << endl;
      Q.push({nx, ny});
    }
  }
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (dist[i][j] == -1) {
        cout << -1;
        return 0;
      }
      ans = max(ans, dist[i][j]);
    }
  }
  cout << ans;
}