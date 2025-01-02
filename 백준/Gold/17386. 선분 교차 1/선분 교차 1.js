const fs = require('fs');
const [[x1, y1, x2, y2], [x3, y3, x4, y4]] = fs
  .readFileSync(0)
  .toString()
  .trim()
  .split('\n')
  .map((line) => line.split(' ').map(Number));

function onSegment(p, q, r) {
  return (
    r.x >= Math.min(p.x, q.x) && r.x <= Math.max(p.x, q.x) && r.y >= Math.min(p.y, q.y) && r.y <= Math.max(p.y, q.y)
  );
}

function cross(o, a, b) {
  return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}

function checkCross(A, B, C, D) {
  const ccw1 = cross(A, B, C);
  const ccw2 = cross(A, B, D);
  const ccw3 = cross(C, D, A);
  const ccw4 = cross(C, D, B);

  if (ccw1 * ccw2 < 0 && ccw3 * ccw4 < 0) return 1;

  return (ccw1 === 0 && onSegment(A, B, C)) ||
    (ccw2 === 0 && onSegment(A, B, D)) ||
    (ccw3 === 0 && onSegment(C, D, A)) ||
    (ccw4 === 0 && onSegment(C, D, B))
    ? 1
    : 0;
}

const points = {
  A: { x: x1, y: y1 },
  B: { x: x2, y: y2 },
  C: { x: x3, y: y3 },
  D: { x: x4, y: y4 },
};

console.log(checkCross(points.A, points.B, points.C, points.D));
