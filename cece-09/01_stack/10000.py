import sys


def get_next(x, r, idx):
    global arr, inc
    s, e = x-r, x+r  # current circle
    ST = []

    # 주어진 모든 원에 대해
    for i in range(N):
        cs, ce = arr[i][0]-arr[i][1], arr[i][0]+arr[i][1]

        # 똑같은 원이라면
        if idx == i:
            continue

        # 만약 원이 외부에 있으면 (동일 크기의 원은 ok)
        if (cs <= s and ce >= e) and not (cs == s and ce == e):
            continue

        if ce <= s or cs >= e:
            continue

        # 첫 번째 원소 삽입
        if len(ST) == 0:
            ST.append(i)
            continue

        # 내부에 있는 모든 원에 대해
        t = ST[-1]
        ts, te = arr[t][0]-arr[t][1], arr[t][0]+arr[t][1]
        if ts <= cs and te >= ce:
            # top이 이미 더 큰 원이다
            continue

        while len(ST) > 0:
            t = ST[-1]
            ts, te = arr[t][0]-arr[t][1], arr[t][0]+arr[t][1]
            if ts >= cs and te <= ce:
                # top이 더 작은 원이다
                ST.pop()
            else:
                break
        ST.append(i)
    return ST


def solve(x, r, idx):
    inners = get_next(x, r, idx)

    if len(inners) == 0:
        return 1

    # 원의 영역와 원의 지름 총합
    tot = 1 if idx != -1 else 0
    tmp = 0
    for i in inners:
        tot += solve(arr[i][0], arr[i][1], i)
        tmp += arr[i][1]*2

    if tmp == r*2 and idx != -1:
        tot += 1
    return tot


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 원의 왼쪽 시작점(start)를 기준으로 오름차순 정렬
arr.sort(key=lambda a: a[0]-a[1])
s = arr[0][0]-arr[0][1]

# 원의 오른쪽 끝점(end)를 기준으로 오름차순 정렬
arr.sort(key=lambda a: a[0]+a[1])
e = arr[-1][0]+arr[-1][1]


answer = solve((s+e)/2, (e-s)/2, -1)
print(answer+1)
