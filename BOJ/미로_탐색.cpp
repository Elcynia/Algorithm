#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int n, m;
string board[102];
int vis[102][102];
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  queue<pair<int, int>> Q;
  cin >> n >> m;
  for (int i = 0; i < n; i++) {
    cin >> board[i];
  }

  for (int i = 0; i < n; i++) {
    fill(vis[i], vis[i] + m, -1);
  }

  Q.push({0, 0});
  vis[0][0] = 0;
  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    for (int i = 0; i < 4; i++) {
      int nx = cur.first + dx[i];
      int ny = cur.second + dy[i];
      if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue;
      if (vis[nx][ny] >= 0 || board[nx][ny] != '1') continue;
      vis[nx][ny] = vis[cur.first][cur.second] + 1;
      Q.push({nx, ny});
    }
  }
  cout << vis[n - 1][m - 1] + 1;
}