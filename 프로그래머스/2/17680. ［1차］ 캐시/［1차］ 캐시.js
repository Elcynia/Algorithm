function solution(cacheSize, cities) {
  if (cacheSize === 0) return cities.length * 5;

  let cache = [];
  let answer = 0;

  cities.forEach((city) => {
    city = city.toLowerCase();
    let idx = cache.indexOf(city);

    if (idx > -1) {
      // cache hit
      cache.splice(idx, 1);
      cache.push(city);
      answer += 1;
    } else {
      // cache miss
      if (cache.length >= cacheSize) {
        cache.shift();
      }
      cache.push(city);
      answer += 5;
    }
  });

  return answer;
}

console.log(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']));
