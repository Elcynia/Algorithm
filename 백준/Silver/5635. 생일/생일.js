const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);

const people = new Array(N);
const originalToString = Object.prototype.toString;
Object.prototype.toString = function () {
  return this.sortKey;
};

for (let i = 1; i <= N; i++) {
  const [name, day, month, year] = input[i].split(' ');
  const sortKey = `${year}${month.padStart(2, '0')}${day.padStart(2, '0')}`;
  people[i - 1] = { name, sortKey };
}
people.sort();
Object.prototype.toString = originalToString;

console.log(people[N - 1].name);
console.log(people[0].name);
