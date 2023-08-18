import sys

N = int(input())
C = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ST = []

cnt = 0

for i in range(N):
    x, r = C[i][0], C[i][1]
    s, e = x-r, x+r

    k = 0  # 반지름이 더 작은 모든 원들의 지름
    p, q = 0, 0
    while len(ST) > 0 and ST[-1][1] < C[i][1]:
        top = ST.pop()
        k += top[1]
        p = min(p, top[0]-top[1])
        q = max(q, top[0]+top[1])
        if p == s and q == e:
            break
    if k == r:
        cnt += 3
        ST.append(C[i])
