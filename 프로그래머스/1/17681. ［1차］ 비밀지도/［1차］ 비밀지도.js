function solution(n, arr1, arr2) {
  return arr1.map((v, i) => {
    const bin1 = v.toString(2).padStart(n, '0');
    const bin2 = arr2[i].toString(2).padStart(n, '0');
    return [...bin1]
      .map((bit, idx) => {
        return bin1[idx] === '1' || bin2[idx] === '1' ? '#' : ' ';
      })
      .join('');
  });
}

console.log(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]));
