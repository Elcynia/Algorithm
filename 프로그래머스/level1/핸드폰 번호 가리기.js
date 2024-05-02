function solution(phone_number) {
  return '*'.repeat(phone_number.slice(0, -4).length) + phone_number.slice(-4);
}

console.log(solution('01033334444'));
