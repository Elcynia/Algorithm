const input = require('fs').readFileSync(0).toString().trim();

function isPrime(num) {
  if (num === 1) return true;

  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function solution(word) {
  let sum = 0;
  for (let char of word) {
    if (char >= 'a' && char <= 'z') {
      sum += char.charCodeAt(0) - 96;
    } else if (char >= 'A' && char <= 'Z') {
      sum += char.charCodeAt(0) - 38;
    }
  }

  return isPrime(sum) ? 'It is a prime word.' : 'It is not a prime word.';
}

console.log(solution(input));
