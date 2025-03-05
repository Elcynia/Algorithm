function solution(n, left, right) {
    var answer = [];

    for (let i = left; i <= right; i++) {
        let row = Math.floor(i / n);  // 행
        let col = i % n;              // 열
        answer.push(Math.max(row, col) + 1); 
    }

    return answer;
}
