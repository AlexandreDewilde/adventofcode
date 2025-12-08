const fs = require('node:fs');

const data = fs.readFileSync('input', 'utf8').trim().split('\n');
for (let i = 0; i < data.length; i++) {
    data[i] = data[i].split(',').map(Number);
}

const parents = [...Array(data.length).keys()];
const ranks = Array(data.length).fill(0);

function find(x) {
    if (parents[x] !== x) {
        parents[x] = find(parents[x]);
    }
    return parents[x];
}

function union(x, y) {
    const rootX = find(x);
    const rootY = find(y);
    
    if (rootX !== rootY) {
        if (ranks[rootX] > ranks[rootY]) {
            parents[rootY] = rootX;
        } else if (ranks[rootX] < ranks[rootY]) {
            parents[rootX] = rootY;
        } else {
            parents[rootY] = rootX;
            ranks[rootX]++;
        }
    }
}

const edges = [];

for (let i = 0; i < data.length; i++) {
    for (let j = i + 1; j < data.length; j++) {
        const distance = (data[i][0] - data[j][0]) ** 2 + (data[i][1] - data[j][1]) ** 2 + (data[i][2] - data[j][2]) ** 2;
        edges.push([distance, i, j]);
    }
}


edges.sort((a, b) => a[0] - b[0]);
let nbComponents = data.length;
let i = 0;
for (const [distance, u, v] of edges) {
    if (find(u) !== find(v)) {
        union(u, v);
        nbComponents--;
    }
    if (nbComponents === 1) {
        console.log(data[u][0] * data[v][0]);
        break;
    }
    i++;
}

