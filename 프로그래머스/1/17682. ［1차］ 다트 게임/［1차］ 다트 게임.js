function solution(dartResult) {
  const bonus = { S: 1, D: 2, T: 3 };
  const scores = [];
  let cur = '';

  for (let i = 0; i < dartResult.length; i++) {
    if (!isNaN(dartResult[i])) {
      cur += dartResult[i];
    } else if (dartResult[i] in bonus) {
      const score = Math.pow(+cur, bonus[dartResult[i]]);
      scores.push(score);
      cur = '';
    } else {
      if (dartResult[i] === '*') {
        scores[scores.length - 1] *= 2;
        if (scores.length > 1) {
          scores[scores.length - 2] *= 2;
        }
      } else if (dartResult[i] === '#') {
        scores[scores.length - 1] *= -1;
      }
    }
  }

  return scores.reduce((sum, curr) => sum + curr, 0);
}

console.log(solution('1S2D*3T'));