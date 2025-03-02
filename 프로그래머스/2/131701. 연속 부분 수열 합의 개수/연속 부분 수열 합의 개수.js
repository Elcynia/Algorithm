function solution(elements) {
  const n = elements.length;
  const uniqueSums = new Set();
  for (let length = 1; length <= n; length++) {
    let sum = 0;

    for (let i = 0; i < length; i++) {
      sum += elements[i];
    }
    uniqueSums.add(sum);

    for (let startIdx = 1; startIdx < n; startIdx++) {
      sum = sum - elements[startIdx - 1] + elements[(startIdx + length - 1) % n];
      uniqueSums.add(sum);
    }
  }

  return uniqueSums.size;
}
