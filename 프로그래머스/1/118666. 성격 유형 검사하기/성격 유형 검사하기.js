function solution(survey, choices) {
  const scores = {
    R: 0,
    T: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    A: 0,
    N: 0,
  };

  const points = [, 3, 2, 1, 0, 1, 2, 3];

  survey.forEach((types, idx) => {
    const choice = choices[idx];

    if (choice < 4) {
      // 비동의 -> 첫 번째 캐릭터에 점수
      scores[types[0]] += points[choice];
    } else if (choice > 4) {
      // 동의 -> 두 번째 캐릭터에 점수
      scores[types[1]] += points[choice];
    }
  });

  let result = '';
  result += scores.R >= scores.T ? 'R' : 'T';
  result += scores.C >= scores.F ? 'C' : 'F';
  result += scores.J >= scores.M ? 'J' : 'M';
  result += scores.A >= scores.N ? 'A' : 'N';

  return result;
}

console.log(solution(['AN', 'CF', 'MJ', 'RT', 'NA'], [5, 3, 2, 7, 5]));
