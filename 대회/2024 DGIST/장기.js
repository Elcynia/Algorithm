const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const 척이 = input[0].split(' ').map(Number);
const 은규 = input[1].split(' ').map(Number);

function calculateScore(pieces) {
  const scores = [13, 7, 5, 3, 3, 2];
  let total = 0;
  for (let i = 0; i < pieces.length; i++) {
    total += pieces[i] * scores[i];
  }

  return total;
}

function determineWinner(cho, han) {
  const choScore = calculateScore(cho);
  const hanScore = calculateScore(han) + 1.5;

  return choScore > hanScore ? 'cocjr0208' : 'ekwoo';
}

console.log(determineWinner(척이, 은규));
