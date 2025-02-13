function solution(cacheSize, cities) {
  if (cacheSize === 0) return cities.length * 5;

  const cache = new Map();
  let answer = 0;

  cities.forEach((city) => {
    city = city.toLowerCase();

    if (cache.has(city)) {
      // cache hit
      cache.delete(city);
      cache.set(city, true);
      answer += 1;
    } else {
      // cache miss
      if (cache.size >= cacheSize) {
        const firstKey = cache.keys().next().value;
        cache.delete(firstKey);
      }
      cache.set(city, true);
      answer += 5;
    }
  });

  return answer;
}

console.log(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']));
