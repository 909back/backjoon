# N, M, K를 공백으로 구분하여 입력받기 
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split()))

data.sort(reverse=True)