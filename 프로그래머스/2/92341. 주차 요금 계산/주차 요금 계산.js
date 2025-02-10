function solution(fees, records) {
  const parkingRecords = new Map();
  const timeRecords = new Map();

  const getMinutes = (time) => {
    const [hours, minutes] = time.split(':').map(Number);
    return hours * 60 + minutes;
  };

  // 입출차 기록 처리
  records.forEach((record) => {
    const [time, carNum, type] = record.split(' ');
    if (type === 'IN') {
      parkingRecords.set(carNum, getMinutes(time));
    } else {
      const inTime = parkingRecords.get(carNum);
      const duration = getMinutes(time) - inTime;
      timeRecords.set(carNum, (timeRecords.get(carNum) || 0) + duration);
      parkingRecords.delete(carNum);
    }
  });

  // 출차 기록이 없는 차량 처리
  parkingRecords.forEach((inTime, carNum) => {
    const duration = getMinutes('23:59') - inTime;
    timeRecords.set(carNum, (timeRecords.get(carNum) || 0) + duration);
  });

  // 요금 계산
  const [baseTime, baseFee, unitTime, unitFee] = fees;
  return [...timeRecords.entries()]
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([_, time]) => {
      if (time <= baseTime) return baseFee;
      return baseFee + Math.ceil((time - baseTime) / unitTime) * unitFee;
    });
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
