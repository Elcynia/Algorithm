const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const arr = input[1].split(' ').map(Number);
const LIS = [arr[0]];
// 각 길이별 최솟값 저장

for (let i = 1; i < N; i++) {
  if (arr[i] > LIS[LIS.length - 1]) {
    LIS.push(arr[i]);
  } else {
    // binary-search
    let left = 0;
    let right = LIS.length - 1;

    while (left < right) {
      let mid = Math.floor((left + right) / 2);
      if (LIS[mid] < arr[i]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    LIS[left] = arr[i];
  }
}

console.log(LIS.length);
