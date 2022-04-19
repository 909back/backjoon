N = list(map(str, input()))

N.sort(reverse=True)

number = ''

for i in N:
    number += i


number = int(number)

if( number % 30 == 0):
    print(number)
else:
    print(-1)

