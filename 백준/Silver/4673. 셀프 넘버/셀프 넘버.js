const N = 10000;
const arr = Array(N + 1).fill(false);

const d = (n) => [...String(n)].reduce((sum, digit) => sum + +digit, n);

for (let i = 1; i <= N; i++) {
  const dn = d(i);
  if (dn <= N) arr[dn] = true;
}

for (let i = 1; i <= N; i++) {
  if (!arr[i]) console.log(i);
}
