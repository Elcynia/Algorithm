const fs = require('fs');
const [n, str] = fs.readFileSync(0).toString().trim().split('\n');

function checkPassword(pwd) {
  let cnt = 0;
  if (!/[a-z]/.test(pwd)) cnt++;
  if (!/[A-Z]/.test(pwd)) cnt++;
  if (!/[0-9]/.test(pwd)) cnt++;
  if (!/[!@#$%^&*()\-+]/.test(pwd)) cnt++;

  // 6글자 이하인지 체크
  const checked = Math.max(0, 6 - pwd.length);

  // 부족한 문자 수와 길이 부족분 중 큰 값을 반환
  return Math.max(checked, cnt);
}

console.log(checkPassword(str));
