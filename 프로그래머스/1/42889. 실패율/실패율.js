function solution(N, stages) {
    let arr = new Array(N+2).fill(0);
    for (const stage of stages) {
        arr[stage] += 1;
    }
    // console.log (arr)
    let total = stages.length
    const fails = {}
    for (let i = 1; i <= N; i++) {
        if (arr[i] === 0) {
            fails[i] = 0;
            continue;
        }
        fails[i] = arr[i] / total;
        total -= arr[i];
    }
    const result = Object.entries(fails).sort((a,b) => b[1] - a[1])
    return result.map(v => Number(v[0]))

}