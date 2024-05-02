#include <bits/stdc++.h>
using namespace std;
#define setio ios::sync_with_stdio(0), cin.tie(0);
#define endl "\n";

int n, cnt, not_cnt = 0;
char board[102][102];
bool vis[102][102];
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};

void init() {
  for (int i = 0; i < n; i++) {
    fill(vis[i], vis[i] + n, false);
  }
}
void bfs(int i, int j) {
  queue<pair<int, int>> Q;
  Q.push({i, j});
  vis[i][j] = true;
  while (!Q.empty()) {
    auto cur = Q.front();
    Q.pop();
    for (int a = 0; a < 4; a++) {
      int nx = cur.first + dx[a];
      int ny = cur.second + dy[a];
      if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
      if (vis[nx][ny] == 1 || board[i][j] != board[nx][ny])
        continue;  // 이미 방문했거나 같은 색이 아닐 경우 필터링
      vis[nx][ny] = true;
      Q.push({nx, ny});
    }
  }
}

int main(void) {
  setio;
  cin >> n;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cin >> board[i][j];
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (!vis[i][j]) {  // 방문하지 않았을 경우 (false)
        bfs(i, j);
        not_cnt++;
      }
    }
  }
  init();  // 방문 초기화
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (board[i][j] == 'G') {
        board[i][j] = 'R';
      }
    }
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (!vis[i][j]) {
        bfs(i, j);
        cnt++;
      }
    }
  }
  cout << not_cnt << " " << cnt;
  return 0;
}
