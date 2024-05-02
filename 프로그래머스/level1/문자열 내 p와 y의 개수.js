function solution(s) {
  let answer = true;
  let p_cnt = 0;
  let y_cnt = 0;
  for (let i = 0; i < s.length; i++) {
    s[i].toLowerCase() === 'p' ? p_cnt++ : undefined;
    s[i].toLowerCase() === 'y' ? y_cnt++ : undefined;
  }

  return p_cnt === y_cnt ? true : false;
}

solution('pPoooyY');
