const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number); // 나무 수, 가져가려 하는 나무의 길이
const trees = input[1].split(' ').map(Number);

let left = 0;
let right = Math.max(...trees);
let result = 0;

while (left <= right) {
  let mid = Math.floor((left + right) / 2);
  let sum = 0;

  for (let tree of trees) {
    if (tree > mid) {
      sum += tree - mid;
    }
  }

  if (sum >= M) {
    result = mid;
    left = mid + 1;
  } else {
    right = mid - 1;
  }
}

console.log(result);