"""
피보나치
* 첫달에는 토끼 두 쌍이 있었다.
* 두달 이상된 토끼는 번식이 가능하다.
* 번식한 토끼 한쌍은 매달 새끼 토끼 한쌍을 낳는다.
* 토끼는 죽지않는다.

피보나치 함수 
fibo[n] = fibo[n-1] + fibo[n-2]

f[0] = 0
f[1] = 1
f[2] = 2
"""

zero = [1,0,1]
one = [0,1,1]

def fibonacci(num):
    length = len(zero)
    if num >= length :
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('{} {}'.format(zero[num], one[num]))

        

T = (int(input()))

for _ in range(T):
    fibonacci(int(input()))

