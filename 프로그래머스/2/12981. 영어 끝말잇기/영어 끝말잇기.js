function solution(n, words) {
    let wordList = new Set();
    wordList.add(words[0]);

    for (let i = 1; i < words.length; i++) {
        let prev = words[i - 1];
        let cur = words[i];

        if (wordList.has(cur) || prev[prev.length - 1] !== cur[0]) {
            let person = (i % n) + 1;  // 몇 번째 사람
            let turn = Math.floor(i / n) + 1;  // 몇 번째 차례
            return [person, turn];
        }
        
        wordList.add(cur);
    }

    return [0, 0];
}
