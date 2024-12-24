const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const n = parseInt(input[0]);
let result = [];
for (let i = 1; i <= n; i++) {
  result.push(input[i].split(' ').map(Number));
}

result.sort((a, b) => {
  const productA = a[1] * a[2] * a[3];
  const productB = b[1] * b[2] * b[3];

  if (productA === productB) {
    const sumA = a[1] + a[2] + a[3];
    const sumB = b[1] + b[2] + b[3];
    if (sumA === sumB) {
      return a[0] - b[0]; // 첫 번째 값 비교
    }
    return sumA - sumB; // 두 번째 값 비교
  }
  return productA - productB; // 첫 번째 값 비교 (product)
});

console.log(
  result
    .slice(0, 3)
    .map((v) => v[0])
    .join(' ')
);
