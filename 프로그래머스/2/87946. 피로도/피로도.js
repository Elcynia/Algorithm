function solution(k, dungeons) {
    let answer = -1;
    const visited = Array(dungeons.length).fill(0);
    
    function DFS(k, level) {
        answer = Math.max(answer, level);
        for (let i = 0; i < dungeons.length; i++) {
            if (!visited[i] && k >= dungeons[i][0]) {
                visited[i] = 1;
                DFS(k - dungeons[i][1], level+1);
                visited[i] = 0;
            }
        }
    }
    DFS(k, 0);
    return answer;
}