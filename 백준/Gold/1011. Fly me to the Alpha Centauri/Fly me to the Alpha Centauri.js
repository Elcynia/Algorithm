const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const T = Number(input[0]);
const result = [];

function minJumps(x, y) {
  const distance = y - x; // 3
  let maxStep = Math.floor(Math.sqrt(distance)); // 가장 큰 이동거리를 결정하는 기준
  let totalSteps = maxStep * 2 - 1;
  const remainingDistance = distance - maxStep * maxStep;

  if (remainingDistance > maxStep) {
    totalSteps += 2;
  } else if (remainingDistance > 0) {
    totalSteps += 1;
  }

  return totalSteps;
}

function solution() {
  for (let i = 1; i <= T; i++) {
    const [x, y] = input[i].split(' ').map(Number);
    result.push(minJumps(x, y));
  }
  return result.join('\n');
}

console.log(solution());
