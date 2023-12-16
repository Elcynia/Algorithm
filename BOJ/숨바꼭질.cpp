#include <bits/stdc++.h>
using namespace std;
#define setio ios::sync_with_stdio(0), cin.tie(0);
#define endl "\n";
// #define fopen freopen("input.txt", "r", stdin);

int n, k;  // 수빈이가 있는 위치, 동생이 있는 위치
int board[100002];
int main(void) {
  setio;
  // fopen;
  cin >> n >> k;
  queue<int> Q;
  fill(board, board + 100002, -1);
  board[n] = 0;
  Q.push(n);
  while (board[k] == -1) {
    auto cur = Q.front();
    Q.pop();
    for (auto i : {cur - 1, cur + 1, cur * 2}) {
      if (i < 0 || i > 100000) continue;  // i가 음수거나 10만 보다 클 경우 패스
      if (board[i] != -1) continue;  // i 값이 -1이 아니면 패스
      // cout << board[i] << " -> " << board[cur] << endl;
      board[i] = board[cur] + 1;
      Q.push(i);
    }
  }
  cout << board[k];
}
