function solution(n) {
  let sum = 0;
  while (!n == 0) {
    let digits = n % 10;
    n = Math.floor(n / 10);
    sum += digits;
  }
  console.log(sum);
  return sum;
}

solution(123);
