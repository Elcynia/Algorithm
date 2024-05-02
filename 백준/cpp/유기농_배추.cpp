#include <bits/stdc++.h>
using namespace std;
#define setio ios::sync_with_stdio(0), cin.tie(0);
#define endl "\n";

int t, n, m, k;
int board[52][52] = {};
bool vis[52][52];
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};
int 배추지렁이 = 0;
// int cnt = 0;
int main(void) {
  setio;
  cin >> t;
  queue<pair<int, int>> Q;

  while (t--) {
    cin >> m >> n >> k;

    for (int i = 0; i < k; i++) {
      int x, y;
      cin >> x >> y;  // x가 열(column)이고 y가 행(row)
      // 입력 데이터와 맵 좌표를 맞추기위해 x <-> y 스왑
      // ex 1 1 0 0 0
      //    0 1 0 0 0
      //    0 0 0 0 1
      // (0,0), (0,1), (1,1), (2,4)
      board[y][x] = 1;  // 양배추 있는 곳은 1로 체크
    }
    int cnt = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (board[i][j] == 1 && !vis[i][j]) {
          vis[i][j] = 1;
          Q.push({i, j});
          while (!Q.empty()) {
            auto cur = Q.front();
            Q.pop();
            for (int i = 0; i < 4; i++) {
              int nx = cur.first + dx[i];
              int ny = cur.second + dy[i];
              if (nx < 0 || ny < 0 || nx >= n || ny >= m)
                continue;  // 범위 필터
              if (vis[nx][ny] == 1 || board[nx][ny] != 1)
                continue;  // 이미 방문했거나 배추가 안 심어져 있는 구간 필터
              vis[nx][ny] = 1;  // 필터링에 안 걸리면 방문 표시하고
              Q.push({nx, ny});  // 현 좌표를 Q에 삽입
            }
          }
          cnt++;
        }
      }
    }
    cout << cnt << endl;
    for (int i = 0; i < n; i++) {
      fill(vis[i], vis[i] + m, 0);
      fill(board[i], board[i] + m, 0);
    }
  }
  return 0;
}