function convertToBase(n, k) {
  let result = '';
  while (n > 0) {
    result = (n % k) + result;
    n = Math.floor(n / k);
  }
  return result;
}

function isPrime(n) {
  if (n <= 1) return false;
  if (n === 2) return true;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

function solution(n, k) {
  const converted = convertToBase(n, k);
  const numbers = converted.split('0').filter((v) => v !== '');
  return numbers.filter((num) => isPrime(Number(num))).length;
}

console.log(solution(437674, 3));
