const input = require('fs').readFileSync(0).toString().trim().split('\n');
const T = Number(input[0]);
let currentLine = 1;

for (let t = 0; t < T; t++) {
  let sounds = input[currentLine++].split(' ');

  // "what does the fox say?" 나올 때까지 반복
  while (true) {
    const line = input[currentLine++];
    if (line === 'what does the fox say?') break;

    const animalSound = line.split(' ')[2];
    sounds = sounds.filter((sound) => sound !== animalSound);
  }

  console.log(sounds.join(' '));
}
