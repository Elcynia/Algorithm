#include <bits/stdc++.h>
using namespace std;
#define setio              \
  ios::sync_with_stdio(0); \
  cin.tie(0);
#define endl "\n";

int n;
string a;
int main(void) {
  cin >> n;
  cin >> a;
  int mx = 0;
  for (int i = 0; i < n; i++) {
    mx += a[i] - '0';
  }
  cout << mx;
}