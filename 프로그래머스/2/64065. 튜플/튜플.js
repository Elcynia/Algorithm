function solution(s) {
  let answer = [];

  const sets = s
    .slice(2, -2)
    .split('},{') 
    .map((set) => set.split(',').map(Number));

  sets.sort((a, b) => a.length - b.length);

  for (let set of sets) {
    for (let num of set) {
      if (!answer.includes(num)) {
        answer.push(num);
        break;
      }
    }
  }
  return answer;
}
