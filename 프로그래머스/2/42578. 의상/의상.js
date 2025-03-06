function solution(clothes) {
    let answer = 1;
    let clothesMap = new Map();
    
    for (let [name, type] of clothes) {
        clothesMap.set(type, (clothesMap.get(type) || 0) + 1);
    }

    
    for (let i of clothesMap.values()) {
        answer *= (i + 1);
    }

    return answer - 1;
}
