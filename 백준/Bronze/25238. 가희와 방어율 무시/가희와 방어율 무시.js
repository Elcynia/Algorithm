const fs = require('fs');
const [a, b] = fs.readFileSync(0).toString().trim().split(' ');
if (Math.floor(a - ( a * (b/100))) < 100) {
    console.log(1);
} else {
    console.log(0);
}