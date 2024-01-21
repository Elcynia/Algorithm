function solution(n) {
  let answer = 0;
  for (let i = 1; i <= n / 2; i++) {
    n % i == 0 ? (answer += i) : answer;
  }
  console.log(answer + n);
  return answer + n;
}

solution(5);
