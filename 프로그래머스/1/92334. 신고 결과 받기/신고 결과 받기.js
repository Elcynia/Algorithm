function solution(id_list, report, k) {
  const reportMap = new Map();
  const countMap = new Map();

  id_list.forEach((id) => {
    reportMap.set(id, new Set());
    countMap.set(id, 0);
  });

  report.forEach((r) => {
    const [reporter, reported] = r.split(' ');
    if (!reportMap.get(reporter).has(reported)) {
      reportMap.get(reporter).add(reported);
      countMap.set(reported, countMap.get(reported) + 1);
    }
  });

  const bannedUsers = id_list.filter((id) => countMap.get(id) >= k);

  return id_list.map((id) => [...reportMap.get(id)].filter((reported) => bannedUsers.includes(reported)).length);
}

console.log(
  solution(
    ['muzi', 'frodo', 'apeach', 'neo'],
    ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi'],
    2
  )
);
