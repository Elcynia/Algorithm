const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);

let youngest = { name: '', birth: 0 };
let oldest = { name: '', birth: Infinity };

for (let i = 1; i <= N; i++) {
  const [name, day, month, year] = input[i].split(' ');
  const birthNumber = Number(year) * 10000 + Number(month) * 100 + Number(day);

  if (birthNumber > youngest.birth) {
    youngest = { name, birth: birthNumber };
  }
  if (birthNumber < oldest.birth) {
    oldest = { name, birth: birthNumber };
  }
}

console.log(youngest.name);
console.log(oldest.name);
