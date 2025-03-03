function isValid(s) {
    let S = [];
    let map = { ')': '(', ']': '[', '}': '{' };

    for (let char of s) {
        if (char === '(' || char === '[' || char === '{') {
            S.push(char);
        } else {
            if (S.length === 0 || S.pop() !== map[char]) {
                return false;
            }
        }
    }
    return S.length === 0;
}

function solution(s) {
    let cnt = 0;
    let arr = s.split('');

    for (let i = 0; i < s.length; i++) {
        if (isValid(arr.join(''))) {
            cnt++;
        }
        arr.push(arr.shift());
    }

    return cnt;
}
