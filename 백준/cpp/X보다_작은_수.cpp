#include <bits/stdc++.h>
using namespace std;

int main(void)
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  int a[10005], n = 0, x = 0;
  cin >> n >> x;
  for (int i = 0; i < n; i++)
    cin >> a[i];
  for (int i = 0; i < n; i++)
    if (a[i] < x)
      cout << a[i] << " ";
}