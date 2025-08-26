const fs = require('fs');
const N = fs.readFileSync(0).toString().trim();
const word = 'SciComLove';

if (N % 2 === 0) {
  console.log(word);
} else {
  console.log(word.split('').reverse().join(''));
}
