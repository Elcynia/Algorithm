const [N, votes] = require('fs').readFileSync(0).toString().trim().split('\n');
const [abstain, sum] = votes
  .split(' ')
  .reduce(([abs, total], v) => (v === '0' ? [abs + 1, total] : [abs, total + +v]), [0, 0]);

console.log(abstain >= N / 2 ? 'INVALID' : sum > 0 ? 'APPROVED' : 'REJECTED');
