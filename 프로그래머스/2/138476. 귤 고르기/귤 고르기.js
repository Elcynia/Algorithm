function solution(k, tangerine) {
    let answer = 0;
    const tangerineDic = {};
    tangerine.forEach(size => {
        tangerineDic[size] = (tangerineDic[size] || 0) + 1;
    });

    const sortedCounts = Object.values(tangerineDic).sort((a, b) => b - a);

    let cnt = 0;
    for (let i of sortedCounts) {
        k -= i;
        cnt++;
        if (k <= 0) break;
    }

    return cnt;
}
