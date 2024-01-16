#include <bits/stdc++.h>
using namespace std;
#define setio              \
  ios::sync_with_stdio(0); \
  cin.tie(0);
#define endl "\n";

int n = 0;
int main() {
  int mx = 0;
  int idx = 0;
  for (int i = 0; i < 9; i++) {
    cin >> n;
    if (n > mx) {
      mx = n;
      idx = i + 1;
    }
  }
  cout << max(mx, n) << "\n" << idx;
}