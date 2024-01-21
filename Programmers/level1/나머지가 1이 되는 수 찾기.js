// function solution(n) {
//   let answer = [];
//   for (let i = 1; i <= n; i++) {
//     n % i === 1 ? answer.push(i) : null;
//   }
//   console.log(Math.min(parseInt(answer)));
// }

// solution(10);

function solution(n) {
  let answer = 0;
  for (let i = 0; i < n; i++) {
    if (n % i === 1) {
      console.log(i);
      return i;
    }
  }
}

solution(10);
