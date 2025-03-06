function solution(clothes) {
    let answer = 1;
    let clothesObj = {}
    
    for (let [name, type] of clothes) {
        clothesObj[type] = (clothesObj[type] || 0) + 1;
    }
    console.log(clothesObj)

    
    for (let i in clothesObj) {
        answer *= (clothesObj[i] + 1);
    }

    return answer - 1;
}
