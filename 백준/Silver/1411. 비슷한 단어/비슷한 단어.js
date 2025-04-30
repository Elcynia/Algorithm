const fs = require('fs');
const [N, ...words] = fs.readFileSync(0).toString().trim().split('\n');

function getPattern(word) {
  const charMap = new Map();
  const pattern = [];
  let nextId = 0;

  for (const char of word) {
    if (!charMap.has(char)) {
      charMap.set(char, nextId++);
    }
    pattern.push(charMap.get(char));
  }

  return pattern.join(',');
}

function countSimilarPairs() {
  const patternMap = new Map();

  for (const word of words) {
    const pattern = getPattern(word);
    patternMap.set(pattern, (patternMap.get(pattern) || 0) + 1);
  }

  let result = 0;

  for (const count of patternMap.values()) {
    if (count >= 2) {
      // nC2 = n * (n-1) / 2
      result += (count * (count - 1)) / 2;
    }
  }

  return result;
}

console.log(countSimilarPairs());
