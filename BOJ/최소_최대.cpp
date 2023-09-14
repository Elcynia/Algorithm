#include <iostream>
using namespace std;

int main(void)
{
  cin.tie(0);
  ios::sync_with_stdio(0);
  int N;
  int arr[1000001];
  int min = 1000000;
  int max = -1000000;
  cin >> N; // 5

  for (int i = 0; i < N; i++)
  {
    cin >> arr[i];
    if (min > arr[i])
      min = arr[i];
    if (max < arr[i])
      max = arr[i];
  }
  cout << min << " " << max;
  return 0;
}