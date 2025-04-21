const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const [U, N] = input[0].split(' ').map(Number);
const priceCounts = Array(U + 1).fill(0);
const priceBidders = Array(U + 1).fill(null);
let minCount = Infinity;
let minPrice = 0;

for (let i = 1; i <= N; i++) {
  const [name, priceStr] = input[i].split(' ');
  const price = parseInt(priceStr);

  priceCounts[price]++;
  if (priceBidders[price] === null) {
    priceBidders[price] = name;
  }
}

for (let price = 1; price <= U; price++) {
  if (priceCounts[price] > 0) {
    if (priceCounts[price] < minCount) {
      minCount = priceCounts[price];
      minPrice = price;
    } else if (priceCounts[price] === minCount && price < minPrice) {
      minPrice = price;
    }
  }
}

console.log(priceBidders[minPrice], minPrice);
