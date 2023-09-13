#include <bits/stdc++.h>
using namespace std;
#define endl '\n';

int main(void)
{
  cin.tie(0);
  ios::sync_with_stdio(0);
  int grade = 0;
  cin >> grade;
  if (grade >= 90)
    cout << 'A';
  else if (grade >= 80)
  {
    cout << 'B';
  }
  else if (grade >= 70)
  {
    cout << 'C';
  }
  else if (grade >= 60)
  {
    cout << 'D';
  }
  else
    cout << 'F';
}