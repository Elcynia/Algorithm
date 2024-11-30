const fs = require('fs');
const [D, H, W] = fs.readFileSync(0).toString().trim().split(' ').map(Number);
const r = Math.sqrt(W * W + H * H);
console.log(parseInt((D * H) / r), parseInt((D * W) / r));
