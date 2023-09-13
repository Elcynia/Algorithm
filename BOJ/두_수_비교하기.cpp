#include <bits/stdc++.h>
using namespace std;
#define endl "\n";

int main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);
  int a, b = 0;
  cin >> a >> b;

  if (a > b)
    cout << ">";
  else if (a < b)
    cout << "<";
  else
    cout << "==";

  return 0;
}