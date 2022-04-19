S = int(input())

cnt = 0
number = 0;

for i in range(1,S+1):
    number += i
    cnt += 1
    if(number > S):
        cnt -= 1
        break;
 


print(cnt);