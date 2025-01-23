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

/**
 * 문제명: 로또의 최고 순위와 최저 순위
 * 1. 0의 개수 세기(zero), 당첨된 수 개수 세기 (cnt)
 * 2. 순위 매핑 (6개 맞우면 1등 (6:1 ...))
 * 3. 최고 순위, 최저 순위 출력
 */
