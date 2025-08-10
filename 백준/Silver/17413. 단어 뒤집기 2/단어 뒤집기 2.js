const fs = require('fs');
const input = fs.readFileSync(0).toString().trim();

function solution(str) {
  const regex = /<[a-z ]+>|[a-z0-9]+/g;

  return str.replace(regex, (match) => {
    if (match.startsWith('<')) {
      return match;
    } else {
      return match.split('').reverse().join('');
    }
  });
}

console.log(solution(input));
