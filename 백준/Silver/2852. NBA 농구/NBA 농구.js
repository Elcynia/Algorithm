const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');
const N = Number(input[0]);
const maxTime = 48 * 60;

let team1Score = 0;
let team2Score = 0;
let team1LeadTime = 0;
let team2LeadTime = 0;
let lastTime = 0;

function convertToSeconds(time) {
  const [m, s] = time.split(':').map(Number);
  return m * 60 + s;
}

function updateLeadTime(start, end) {
  const duration = end - start;
  if (team1Score > team2Score) {
    team1LeadTime += duration;
  } else if (team2Score > team1Score) {
    team2LeadTime += duration;
  }
}

function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = seconds % 60;
  return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
}

for (let i = 1; i <= N; i++) {
  const [team, time] = input[i].split(' ');
  const currentTime = convertToSeconds(time);

  updateLeadTime(lastTime, currentTime);

  if (team === '1') {
    team1Score++;
  } else {
    team2Score++;
  }

  lastTime = currentTime;
}

updateLeadTime(lastTime, maxTime);

console.log(formatTime(team1LeadTime));
console.log(formatTime(team2LeadTime));
