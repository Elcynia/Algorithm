#include <bits/stdc++.h>
#define endl "\n";
using namespace std;

int main(void)
{
  cin.tie(0);
  ios::sync_with_stdio(0);
  stack<int> S;
  int n;
  cin >> n;
  while (n--)
  {
    string s;
    cin >> s;
    if (s == "push")
    {
      int t;
      cin >> t;
      S.push(t);
    }
    else if (s == "pop")
    {
      if (S.empty())
      {
        cout << -1 << endl;
      }
      else
      {
        cout << S.top() << endl;
        S.pop();
      }
    }
    else if (s == "size")
    {
      cout << S.size() << endl;
    }
    else if (s == "empty")
    {
      cout << (int)S.empty() << endl;
    }
    else
    {
      if (S.empty())
      {
        cout << -1 << endl;
      }
      else
        cout << S.top() << endl;
    }
  }
}
