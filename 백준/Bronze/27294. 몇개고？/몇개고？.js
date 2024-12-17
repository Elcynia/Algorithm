const fs = require('fs');
const [時間, 酒] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
if (時間 >= 12 && 時間 <= 16 && 酒 === 0) {
  console.log(320);
} else {
  console.log(280);
}
