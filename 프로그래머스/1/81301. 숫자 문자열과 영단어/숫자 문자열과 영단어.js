function solution(s) {
    const numberDictionary = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    };

    let result = '';
    let temp = '';

    for (let char of s) {
        if (!isNaN(char)) {
            // 숫자는 그대로 추가
            result += char;
        } else {
            temp += char;
            if (numberDictionary[temp]) {
                result += numberDictionary[temp];
                temp = '';
            }
        }
    }

    return Number(result);
}
