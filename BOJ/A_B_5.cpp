#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int main(void)
{
  cin.tie(nullptr);
  ios::sync_with_stdio(0);
  int a, b;
  while (true)
  {
    cin >> a >> b;
    if (a == 0 && b == 0)
      break;
    cout << a + b << endl;
  }
}