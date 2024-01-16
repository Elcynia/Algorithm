#include <bits/stdc++.h>
using namespace std;

// 하노이의 탑 이동 순서 출력 함수
void hanoi(int n, int from, int mid, int to) {
  if (n == 1) {
    cout << from << " " << to << '\n';
    return;
  }

  // 1. N-1개의 원판을 시작 기둥에서 중간 기둥으로 옮김
  hanoi(n - 1, from, to, mid);

  // 2. 시작 기둥에서 목표 기둥으로 제일 큰 원판을 옮김
  cout << from << " " << to << '\n';

  // 3. 중간 기둥에서 목표 기둥으로 N-1개의 원판을 옮김
  hanoi(n - 1, mid, from, to);
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);

  int n;
  cin >> n;

  // 이동 횟수 출력
  cout << (int)pow(2, n) - 1 << '\n';

  // 하노이 탑 이동 순서 출력
  hanoi(n, 1, 2, 3);

  return 0;
}
