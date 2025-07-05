const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = input.shift();

for (let i of input) {
  if (i === 'Algorithm') console.log(204);
  else if (i == 'Network') console.log(303);
  else if (i == 'CyberSecurity') console.log("B101");
  else if (i == 'Startup') console.log(501);
  else if (i == 'DataAnalysis') console.log(207);
  else if (i == 'ArtificialIntelligence') console.log(302);
  else if (i == 'TestStrategy') console.log(105);
}