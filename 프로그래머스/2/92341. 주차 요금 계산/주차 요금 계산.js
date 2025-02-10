function solution(fees, records) {
  const [baseTime, baseFee, unitTime, unitFee] = fees;
  const parking = {};
  const times = {};

  const getMin = (t) => t.split(':').reduce((h, m) => h * 60 + +m);

  records.forEach((record) => {
    const [time, car, type] = record.split(' ');
    if (type === 'IN') {
      parking[car] = getMin(time);
    } else {
      times[car] = (times[car] || 0) + getMin(time) - parking[car];
      delete parking[car];
    }
  });

  Object.entries(parking).forEach(([car, inTime]) => {
    times[car] = (times[car] || 0) + getMin('23:59') - inTime;
  });

  return Object.entries(times)
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([, t]) => baseFee + (t > baseTime ? Math.ceil((t - baseTime) / unitTime) * unitFee : 0));
}

console.log(
  solution(
    [180, 5000, 10, 600], // 기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)
    [
      '05:34 5961 IN',
      '06:00 0000 IN',
      '06:34 0000 OUT',
      '07:59 5961 OUT',
      '07:59 0148 IN',
      '18:59 0000 IN',
      '19:09 0148 OUT',
      '22:59 5961 IN',
      '23:00 5961 OUT',
    ]
  )
);
