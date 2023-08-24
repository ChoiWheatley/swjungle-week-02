'''
Knapsack Problem
* P[n][k] = 무게 제한이 k일 때, n개의 물건을 knapsack에 담아 얻을 수 있는 최대 가치
* 0-1은 NP-hard, Fraction은 다항 시간 내 솔루션이 있음

* 동전 문제는 무게의 제한이 없는 경우 (각각의 동전은 몇 개라도 사용할 수 있다)
* n개의 물건을 사용해 k가치를 만들 때, 최소의 무게를 구하시오
'''

import sys
inf = float('inf')
N, K = map(int, input().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
dp = [inf for _ in range(K+1)]  # i+1의 가치를 얻기 위한 최소의 동전 수


# 중복된 동전 제거
coins = list(set(coins))

dp[0] = 0
for coin in coins:
    for i in range(1, K+1):
        if i >= coin:  # 이 동전을 사용할 수 있다.
            # coin을 한 번 사용하므로
            # i-coin을 만들기 위한 최소의 동전 수에 1을 더해줌
            dp[i] = min(dp[i], dp[i-coin]+1)

print(dp[K] if dp[K] != inf else -1)
