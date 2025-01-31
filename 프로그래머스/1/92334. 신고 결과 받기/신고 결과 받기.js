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

/**
 * 각 사용자가 신고한 사용자 목록, 신고당한 횟수 저장
 * id_list를 순회하며 모든 사용자의 신고 목록과 신고 횟수를 0으로 초기화
 * report를 순회하며 신고 체크
 * 만약 reporter가 reported를 신고한 적이 없으면 reporter에 추가 (+ count도 +1)
 */
