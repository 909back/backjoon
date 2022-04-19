
city = int(input())
distance = list(map(int,input().split()))
cost = list(map(int,input().split()))

total = 0

minCost = cost[0]

for i in range(city-1):
    if(minCost <= cost[i+1]):
        total += distance[i] * cost[i] 
    elif(minCost > cost[i+1]):
        minCost = cost[i]
        total += minCost * distance[i]

print(total)



