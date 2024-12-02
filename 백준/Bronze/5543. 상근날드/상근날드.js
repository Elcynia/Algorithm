const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const hamburgers = [];
const drinks = [];

for (let i = 0; i < 3; i++) {
  hamburgers.push(+input[i]);
}

for (let i = 3; i < 5; i++) {
  drinks.push(+input[i]);
}

let minPrice = Infinity;

for (let burger of hamburgers) {
  for (let drink of drinks) {
    const setPrice = burger + drink - 50;
    if (setPrice < minPrice) {
      minPrice = setPrice;
    }
  }
}

console.log(minPrice);
