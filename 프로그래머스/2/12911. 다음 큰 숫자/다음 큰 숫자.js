function solution(n) {
    let next = n + 1;
    while (next.toString(2).split('1').length - 1 !== n.toString(2).split('1').length - 1) {
        next++;
    }
    return next;
}
