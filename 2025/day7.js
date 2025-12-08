const fs = require('node:fs');

const grid = fs.readFileSync('input', 'utf8').trim().split('\n');

const mem = {};
function dp(i, c) {
    if (mem[[i, c]]) return mem[[i, c]];
    if (i === grid.length) return 1;
    if (grid[i][c] === '^') {
        let res = 0;
        if (i + 1 < grid.length && c + 1 < grid[i].length && grid[i + 1][c + 1] !== '^') {
            res += dp(i + 1, c + 1);
        }
        if (i + 1 < grid.length && c - 1 >= 0 && grid[i + 1][c - 1] !== '^') {
            res += dp(i + 1, c - 1);
        }
        mem[[i, c]] = res;
        return mem[[i, c]];
    }
    mem[[i, c]] = dp(i + 1, c);
    return mem[[i, c]];
}

const start = grid[0].indexOf('S'); 
console.log(dp(0, start));