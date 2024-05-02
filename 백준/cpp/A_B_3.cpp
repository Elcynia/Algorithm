#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int main(void)
{
  cin.tie(nullptr);
  ios::sync_with_stdio(0);
  int t, a[10005], b[10005];
  cin >> t;
  for (int i = 0; i < t; i++)
  {
    cin >> a[i] >> b[i];
  }

  for (int i = 0; i < t; i++)
  {
    cout << a[i] + b[i] << endl;
  }
}