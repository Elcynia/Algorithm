const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const T = +input[0];
const scores = input[1].split(' ').map(Number);

const kor = scores[0] || 0;
const math = scores[1] || 0;
const eng = scores[2] || 0;
const inquiry = scores[3] || 0;
const foreignLang = scores[4] || 0;

let res1 = Math.abs(kor - eng) * (kor > eng ? 508 : 108);
let res2 = Math.abs(math - inquiry) * (math > inquiry ? 212 : 305);
let res3 = foreignLang * 707; // 제2외국어가 없으면 0

const studentId = (res1 + res2 + res3) * 4763;
console.log(studentId);
