const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const angles = input.map(Number);
const sum = angles.reduce((acc, curr) => acc + curr, 0);
const equal = angles[0] === angles[1] || angles[1] === angles[2] || angles[0] === angles[2];

if (angles[0] === 60 && angles[1] === 60 && angles[2] === 60) {
  console.log('Equilateral');
} else if (sum === 180) {
  if (equal) {
    console.log('Isosceles');
  } else {
    console.log('Scalene');
  }
} else {
  console.log('Error');
}
