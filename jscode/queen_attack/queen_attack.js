'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'queensAttack' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER r_q
 *  4. INTEGER c_q
 *  5. 2D_INTEGER_ARRAY obstacles
 */

const DEBUG = 0;
function show(x) {
    if (DEBUG == 1) console.log(x)
}

function queensAttack(n, k, r_q, c_q, obstacles) {
    // Write your code here
    obstacles = new Set(obstacles.map(x => x.toString()))
    let count = 0;
    // down
    for (var k=r_q-1; k>0; k--) {
        var cur = [k, c_q].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }

    // up 
    for (var k=r_q+1; k<=n; k++) {
        var cur = [k, c_q].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }

    // left 
    for (var k=c_q-1; k>0; k--) {
        var cur = [r_q, k].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }

    // right
    for (var k=c_q+1; k<=n; k++) {
        var cur = [r_q, k].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }

    // NE
    for (var k=r_q+1, j=c_q+1; k<=n && j<=n; k++, j++) {
        var cur = [k, j].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }

    // SW
    for (var k=r_q-1, j=c_q-1; k>0 && j>0; k--, j--) {
        var cur = [k, j].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }

    // SE
    for (var k=r_q-1, j=c_q+1; k>0 && j<=n; k--, j++) {
        var cur = [k, j].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }

    // NW 
    for (var k=r_q+1, j=c_q-1; k<=n && j>0; k++, j--) {
        var cur = [k, j].toString()
        if (obstacles.has(cur)) {
            break
        } else {
            count++;
        }
    }
    return count

}

function main() {
    // const ws = fs.createWriteStream(process.env.OUTPUT_PATH);
    // const ws = fs.createWriteStream("./data/input.txt")

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');
    const n = parseInt(firstMultipleInput[0], 10);
    const k = parseInt(firstMultipleInput[1], 10);

    const secondMultipleInput = readLine().replace(/\s+$/g, '').split(' ');
    const r_q = parseInt(secondMultipleInput[0], 10);
    const c_q = parseInt(secondMultipleInput[1], 10);

    let obstacles = Array(k);

    for (let i = 0; i < k; i++) {
        obstacles[i] = readLine().replace(/\s+$/g, '').split(' ').map(obstaclesTemp => parseInt(obstaclesTemp, 10));
    }

    const result = queensAttack(n, k, r_q, c_q, obstacles);
    console.log(result)

    // ws.write(result + '\n');
    // ws.end();
}
