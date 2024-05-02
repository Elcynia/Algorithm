#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int 격자판[502][502];
bool 방문[502][502];
int dx[4] = {0, 1, -1, 0};
int dy[4] = {1, 0, 0, -1};
int 행, 열;
int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> 행 >> 열;
  for (int i = 0; i < 행; i++) {  // 격자판 입력받기 (6*5)
    for (int j = 0; j < 열; j++) {
      cin >> 격자판[i][j];
    }
  }
  int 가장넓은그림너비 = 0;
  int 그림수 = 0;
  for (int i = 0; i < 행; i++) {
    for (int j = 0; j < 열; j++) {
      cin >> 방문[i][j];
      if (방문[i][j] == 1 or 격자판[i][j] == 0) continue;
      그림수++;
      queue<pair<int, int>> Q;
      방문[i][j] = 1;
      Q.push({i, j});
      int 너비 = 0;  // 그림의 넓이
      while (!Q.empty()) {
        너비++;
        pair<int, int> cur = Q.front();
        Q.pop();
        for (int i = 0; i < 4; i++) {
          int nx = cur.first + dx[i];
          int ny = cur.second + dy[i];
          if (nx < 0 || ny >= 열 || nx >= 행 || ny < 0) continue;
          if (방문[nx][ny] || 격자판[nx][ny] != 1) continue;
          방문[nx][ny] = 1;
          Q.push({nx, ny});
        }
      }
      가장넓은그림너비 = max(가장넓은그림너비, 너비);
    }
  }
  cout << 그림수 << "\n" << 가장넓은그림너비;
}