#include <bits/stdc++.h>
using namespace std;
#define setio              \
  ios::sync_with_stdio(0); \
  cin.tie(0);
#define endl "\n";

int n;
int main(void) {
  int a = 0;
  string b;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a >> b;
    for (int i = 0; i < a; i++) {
      cout << b;
    }
  }
}