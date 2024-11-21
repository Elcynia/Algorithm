const fs = require('fs');

function sumDigits(num, base) {
  let sum = 0;
  while (num > 0) {
    sum += num % base;
    num = Math.floor(num / base);
  }
  return sum;
}

function findSpecialNumbers() {
  for (let i = 2992; i <= 9999; i++) {
    const sum10 = sumDigits(i, 10);
    const sum12 = sumDigits(i, 12);
    const sum16 = sumDigits(i, 16);

    if (sum10 === sum12 && sum12 === sum16) {
      console.log(i);
    }
  }
}

findSpecialNumbers();
