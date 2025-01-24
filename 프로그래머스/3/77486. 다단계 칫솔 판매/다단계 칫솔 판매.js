function solution(enroll, referral, seller, amount) {
  const memberTree = new Map();
  const profits = new Map();

  // 관계도 및 수익 초기화
  enroll.forEach((name, i) => {
    memberTree.set(name, referral[i]);
    profits.set(name, 0);
  });

  // 판매 수익 계산 및 분배
  seller.forEach((name, i) => {
    let money = amount[i] * 100;
    let current = name;

    while (current !== '-' && money > 0) {
      const profit = Math.floor(money * 0.1);
      profits.set(current, profits.get(current) + (money - profit));
      money = profit;
      current = memberTree.get(current);
    }
  });

  return enroll.map((name) => profits.get(name));
}

const enroll = ['john', 'mary', 'edward', 'sam', 'emily', 'jaimie', 'tod', 'young'];
const referral = ['-', '-', 'mary', 'edward', 'mary', 'mary', 'jaimie', 'edward'];
const seller = ['young', 'john', 'tod', 'emily', 'mary']; // 판매원
const amount = [12, 4, 2, 5, 10]; // 판매 수량

console.log(solution(enroll, referral, seller, amount));
