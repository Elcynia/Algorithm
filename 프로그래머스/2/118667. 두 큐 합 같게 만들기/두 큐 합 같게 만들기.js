function solution(queue1, queue2) {
  let sum1 = queue1.reduce((a, b) => a + b, 0);
  let sum2 = queue2.reduce((a, b) => a + b, 0);
  const target = (sum1 + sum2) / 2;

  if ((sum1 + sum2) % 2 !== 0) return -1;

  let count = 0;
  let p1 = 0,
    p2 = 0;
  const q1 = [...queue1],
    q2 = [...queue2];
  const maxCount = (queue1.length + queue2.length) * 2;

  while (count <= maxCount) {
    if (sum1 === target) return count;

    if (sum1 > target && p1 < queue1.length + queue2.length) {
      sum1 -= q1[p1];
      sum2 += q1[p1];
      q2.push(q1[p1]);
      p1++;
    } else if (sum1 < target && p2 < queue1.length + queue2.length) {
      sum1 += q2[p2];
      sum2 -= q2[p2];
      q1.push(q2[p2]);
      p2++;
    } else {
      break;
    }
    count++;
  }

  return -1;
}

console.log(solution([3, 2, 7, 2], [4, 6, 5, 1]));
