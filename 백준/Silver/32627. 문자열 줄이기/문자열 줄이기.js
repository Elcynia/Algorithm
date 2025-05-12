const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const [N, M] = input.shift().split(' ').map(Number);
const S = input[0].split('');

if (M === 0) {
  console.log(S.join(''));
} else {
  const obj = S.map((char, index) => ({ char, index }));

  obj.sort((a, b) => {
    if (a.char < b.char) return -1;
    if (a.char > b.char) return 1;
    return a.index - b.index;
  });

  const idxArr = new Set();
  for (let i = 0; i < M; i++) {
    idxArr.add(obj[i].index);
  }

  let result = '';
  for (let i = 0; i < S.length; i++) {
    if (!idxArr.has(i)) {
      result += S[i];
    }
  }
  console.log(result);
}
