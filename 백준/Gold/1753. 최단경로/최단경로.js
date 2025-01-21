const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n');

const [V, E] = input[0].split(' ').map(Number);
const K = parseInt(input[1]);
const edges = input.slice(2).map((line) => line.split(' ').map(Number));

const INF = 1e12;
const adjList = Array.from({ length: V + 1 }, () => []);
const dist = Array(V + 1).fill(INF);

for (const [u, v, w] of edges) {
  adjList[u].push([v, w]);
}

class PriorityQueue {
  constructor() {
    this.values = [];
  }

  push(element) {
    this.values.push(element);
    this._bubbleUp(this.values.length - 1);
  }

  pop() {
    if (this.values.length === 0) return null;
    if (this.values.length === 1) return this.values.pop();

    const min = this.values[0];
    this.values[0] = this.values.pop();
    this._bubbleDown(0);
    return min;
  }

  _bubbleUp(index) {
    while (index > 0) {
      const parentIdx = Math.floor((index - 1) / 2);
      if (this.values[parentIdx][0] <= this.values[index][0]) break;
      [this.values[parentIdx], this.values[index]] = [this.values[index], this.values[parentIdx]];
      index = parentIdx;
    }
  }

  _bubbleDown(index) {
    const length = this.values.length;
    while (true) {
      let minIndex = index;
      const leftChild = 2 * index + 1;
      const rightChild = 2 * index + 2;

      if (leftChild < length && this.values[leftChild][0] < this.values[minIndex][0]) {
        minIndex = leftChild;
      }
      if (rightChild < length && this.values[rightChild][0] < this.values[minIndex][0]) {
        minIndex = rightChild;
      }
      if (minIndex === index) break;

      [this.values[index], this.values[minIndex]] = [this.values[minIndex], this.values[index]];
      index = minIndex;
    }
  }

  isEmpty() {
    return this.values.length === 0;
  }
}

const dijkstra = (start) => {
  const pq = new PriorityQueue();
  const visited = new Array(V + 1).fill(false);
  dist[start] = 0;
  pq.push([0, start]);

  while (!pq.isEmpty()) {
    const [curDist, curNode] = pq.pop();

    if (visited[curNode]) continue;
    visited[curNode] = true;

    for (const [adjNode, adjDist] of adjList[curNode]) {
      if (visited[adjNode]) continue;
      const newDist = curDist + adjDist;
      if (newDist < dist[adjNode]) {
        dist[adjNode] = newDist;
        pq.push([newDist, adjNode]);
      }
    }
  }
};

dijkstra(K);

dist.slice(1).forEach((d) => {
  console.log(d === INF ? 'INF' : d);
});
