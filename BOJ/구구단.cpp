#include <bits/stdc++.h>
using namespace std;
#define endl '\n';

int main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);
  int n = 0;
  cin >> n;
  for (int i = 1; i <= 9; i++)
  {
    cout << n << " * " << i << " = " << n * i << "\n";
  }
}
