const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = +input[0];
const runners = new Set();

for (let i = 1; i <= N; i++) {
  const name = input[i];
  runners[name] = (runners[name] || 0) + 1;
}

for (let i = N + 1; i < input.length; i++) {
  const name = input[i];
  runners[name]--;
}

for (let name in runners) {
  if (runners[name] === 1) {
    console.log(name);
    break;
  }
}
