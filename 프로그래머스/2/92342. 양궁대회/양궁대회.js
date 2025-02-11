function getCurPoint(apeach, lion) {
  let apeachPoint = 0;
  let lionPoint = 0;

  for (let i = 0; i < 11; i++) {
    if (apeach[i] === 0 && lion[i] === 0) continue;
    if (apeach[i] >= lion[i]) {
      apeachPoint += 10 - i;
    } else {
      lionPoint += 10 - i;
    }
  }
  return lionPoint - apeachPoint;
}

function* combinationsWithReplacement(arr, n) {
  const len = arr.length;
  function* generate(pos, count, current) {
    if (count === n) {
      yield current.slice();
      return;
    }
    for (let i = pos; i < len; i++) {
      current.push(arr[i]);
      yield* generate(i, count + 1, current);
      current.pop();
    }
  }
  yield* generate(0, 0, []);
}

function solution(n, info) {
  let bestPoint = 0;
  let bestResult = Array(11).fill(0);
  const scores = Array.from({ length: 11 }, (_, i) => i);

  for (const comb of combinationsWithReplacement(scores, n)) {
    const curResult = Array(11).fill(0);

    comb.forEach((num) => curResult[num]++);

    const curPoint = getCurPoint(info, curResult);
    const isBetter =
      curPoint > bestPoint ||
      (curPoint === bestPoint && curResult.slice().reverse().join(',') > bestResult.slice().reverse().join(','));

    if (isBetter) {
      bestPoint = curPoint;
      bestResult = [...curResult];
    }
  }

  return bestPoint === 0 ? [-1] : bestResult;
}

console.log(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]));
