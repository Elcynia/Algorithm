#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int n, m;
string board[1002];    // 격자판
int fire[1002][1002];  // 불 거리 계산용
int dist[1002][1002];  // J 거리 계산용
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n >> m;
  queue<pair<int, int>> Q1;  // fire (F)
  queue<pair<int, int>> Q2;  // dist (J)

  for (int i = 0; i < n; i++) {
    cin >> board[i];
  }
  for (int i = 0; i < n; i++) {
    fill(fire[i], fire[i] + m, -1);
    fill(dist[i], dist[i] + m, -1);
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (board[i][j] == 'F') {
        Q1.push({i, j});
        fire[i][j] = 0;
      }
      if (board[i][j] == 'J') {
        Q2.push({i, j});
        dist[i][j] = 0;
      }
    }
  }

  while (!Q1.empty()) {
    auto cur = Q1.front();
    Q1.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.first + dx[i];
      int ny = cur.second + dy[i];
      if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
      if (fire[nx][ny] >= 0 || board[nx][ny] == '#') continue;
      fire[nx][ny] = fire[cur.first][cur.second] + 1;
      Q1.push({nx, ny});
    }
  }

  while (!Q2.empty()) {
    auto cur = Q2.front();
    Q2.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.first + dx[i];
      int ny = cur.second + dy[i];
      if (nx < 0 || ny < 0 || nx >= n || ny >= m) {
        cout << dist[cur.first][cur.second] + 1;
        return 0;
      }
      if (dist[nx][ny] >= 0 || board[nx][ny] == '#') continue;
      if (fire[nx][ny] != -1 && fire[nx][ny] <= dist[cur.first][cur.second] + 1)
        continue;  // J가 가려는 타이밍에 이미 불 전파가 되었을 때의 처리조건
      dist[nx][ny] = dist[cur.first][cur.second] + 1;
      Q2.push({nx, ny});
    }
  }
  cout << "IMPOSSIBLE";
}