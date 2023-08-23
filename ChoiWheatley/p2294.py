"""
동전 2

DP문제잖아
"""

INF = 99999

n, k = [int(x) for x in input().split()]
coins = [int(input()) for _ in range(n)]


# dp[i]: i원을 만들기 위해 필요한 최소한의 동전개수
# dp[0] = 0
# dp[k] = min(dp[k - coin] + 1 for coin in coins)
dp = [INF for _ in range(k + 1)]

dp[0] = 0

for i in range(1, k + 1):
    for coin in coins:
        if coin - i > 0:
            continue
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != INF else -1)
