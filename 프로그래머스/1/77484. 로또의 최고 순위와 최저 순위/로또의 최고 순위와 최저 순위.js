function solution(lottos, win_nums) {
  let zero = 0;
  for (let num of lottos) {
    if (num === 0) zero++;
  }

  let cnt = 0;
  for (let num of lottos) {
    if (win_nums.includes(num)) cnt++;
  }

  const cntToRank = { 6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6 };

  return [cntToRank[cnt + zero], cntToRank[cnt]];
}

console.log(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]));
