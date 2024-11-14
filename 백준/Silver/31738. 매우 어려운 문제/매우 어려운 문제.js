const fs = require('fs');
const [n, m] = fs.readFileSync(0).toString().trim().split(' ').map(Number);

function main() {
  if (n > m) {
    console.log(0);
  } else {
    if (n === 1) {
      console.log(1);
    } else {
      let fact = 1;
      for (let i = 2; i <= n; i++) {
        fact = (fact * i) % m;
      }
      console.log(fact.toString());
    }
  }
}

main();
