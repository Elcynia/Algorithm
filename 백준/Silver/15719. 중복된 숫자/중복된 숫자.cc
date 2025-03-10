#include <bits/stdc++.h>
using namespace std;
#define setio              \
  ios::sync_with_stdio(0); \
  cin.tie(0);
#define endl "\n"

int main() {
  setio;
  
  int n;
  cin >> n;
  
  long long expected_sum = (long long)(n-1) * n / 2;
  long long actual_sum = 0;
  int num;
  
  for (int i = 0; i < n; i++) {
    cin >> num;
    actual_sum += num;
  }
  
  cout << actual_sum - expected_sum << endl;
  return 0;
}
