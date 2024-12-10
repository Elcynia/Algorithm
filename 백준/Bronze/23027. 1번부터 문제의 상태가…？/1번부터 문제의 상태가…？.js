const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();

function modifyLetter(letter) {
  if (letter.includes('A')) {
    return letter.replace(/[BCDF]/g, 'A');
  } else if (letter.includes('B')) {
    return letter.replace(/[CDF]/g, 'B');
  } else if (letter.includes('C')) {
    return letter.replace(/[DF]/g, 'C');
  } else {
    return 'A'.repeat(letter.length);
  }
}

console.log(modifyLetter(input));
