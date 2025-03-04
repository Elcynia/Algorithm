function solution(want, number, discount) {
    let wantMap = new Map();
    let cnt = 0;
    
    for (let i = 0; i < want.length; i++) {
        wantMap.set(want[i], number[i]);
    }
    
    // 슬라이딩 윈도우
    for (let i = 0; i <= discount.length - 10; i++) {
        let windowMap = new Map();
        
        // 현재 10일 동안의 제품 개수를 계산
        for (let j = i; j < i + 10; j++) {
            windowMap.set(discount[j], (windowMap.get(discount[j]) || 0) + 1);
        }
        
        // 원하는 제품 목록과 비교
        let isMatch = true;
        for (let [key, value] of wantMap) {
            if (windowMap.get(key) !== value) {
                isMatch = false;
                break;
            }
        }
        
        if (isMatch) cnt++;
    }
    
    return cnt;
}