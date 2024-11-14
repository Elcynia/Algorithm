const fs = require('fs');
const [n, m] = fs.readFileSync(0).toString().trim().split(' ').map(BigInt);

function main() {
  if (n > m) {
    console.log(0);
  } else {
    if (n === 1n) {
      console.log(1);
    } else {
      let fact = 1n;
      for (let i = 2n; i <= n; i++) {
        fact = (fact * i) % m;
      }
      console.log(fact.toString());
    }
  }
}

main();
