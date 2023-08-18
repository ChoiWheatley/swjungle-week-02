N, K = map(int, input().split())
X = list(map(int, input()))  # 자리수로 분할


ST = []
delcnt = 0
for i in range(N):
    if not len(ST):  # push if empty
        ST.append(X[i])
        continue

    if X[i] > ST[-1] and delcnt < K:
        top = ST[-1]
        while X[i] > top:
            ST.pop()
            delcnt += 1
            if not len(ST) or delcnt == K:
                break
            top = ST[-1]

    ST.append(X[i])

print("".join(list(map(str, ST[:(N-K)]))))
