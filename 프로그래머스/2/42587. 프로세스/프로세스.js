function solution(priorities, location) {
  let answer = 0;

  const Q = priorities.map((item, idx) => ({
    item,
    idx,
  }));

  while (Q.length > 0) {
    const cur = Q.shift();

    const check = Q.some((p) => p.item > cur.item);

    if (check) {
      Q.push(cur);
    } else {
      // 없으면 카운트 증가
      answer++;

      if (cur.idx === location) {
        return answer;
      }
    }
  }

  return answer;
}