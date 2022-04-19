/**
 * DP 중 Bottom-up 방식 
 * 
 * 가능한 연산을 통해 얻을 수 있는 이전 숫자들을 1로 만드는 최소 연산 횟수들 중 가장 작은 값 + 1(앞에서 한 연산)
 */

const input = require('fs').readFileSync('/dev/stdin').toString();

const num = Number(input);

const DP = new Array(num+1).fill(0);

for (let i = 2; i < DP.length; i++){
    DP[i] = DP[i-1]+1;
    
    if(i % 3 === 0){
        DP[i] = Math.min(DP[i],DP[i / 3]+1);
    } 
    
    if(i%2 === 0){
        DP[i] = Math.min(DP[i],DP[i/2]+1);
    }
}

console.log(DP[num]);