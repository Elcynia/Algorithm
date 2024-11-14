let [n, m] = require("fs")
  .readFileSync("./dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map((v) => Number(v))

function factorialMod(n, m) {
  let result = 1

  for (let i = 1; i <= n; i++) {
    result *= i
    result %= m
  }

  return result
}
if (n >= m) console.log(0)
else console.log(factorialMod(n, m))