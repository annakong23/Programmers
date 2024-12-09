n = int(input())

prices = list(map(int, input().split()))

dp = [0] * 1001

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j]+prices[j-1]) #list인덱스 0부터니까
        
print(dp[n])