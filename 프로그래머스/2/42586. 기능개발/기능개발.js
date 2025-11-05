function solution(progresses, speeds) {
  let answer = [];
  let Q = [];
  for (let i = 0; i < progresses.length; i++) {
    let days = Math.ceil((100 - progresses[i]) / speeds[i]);
    Q.push(days);
  }

  let cnt = 1;
  let prev = Q[0];
  for (let i = 1; i < Q.length; i++) {
    if (Q[i] <= prev) {
      cnt++;
    } else {
      answer.push(cnt);
      cnt = 1;
      prev = Q[i];
    }
  }
  answer.push(cnt);

  return answer;
}
