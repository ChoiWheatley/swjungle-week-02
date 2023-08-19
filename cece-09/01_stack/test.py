import sys


N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# x좌표를 기준으로 정렬
arr.sort(key=lambda a: a[0])


ST = []

# 주어진 모든 원에 대해 차례대로 검사

tmp = 0  # 내부 반지름을 합산하는 데 사용
ans = 0  # 영역 합산
p = -1  # 직전 원 인덱스

# first push
ST.append(0)
for i in range(N):
    ans += 1
    s, e = arr[i][0]-arr[i][1], arr[i][0]+arr[i][1]

    # # 내부에 있는 모든 원에 대해
    # t = ST[-1]
    # ts, te = arr[t][0]-arr[t][1], arr[t][0]+arr[t][1]

    # top이 오른쪽 내부에 속함
    # if ts <= s and arr[t][0] <= te:
    #     k += arr[i][1]
    #     print(f"[{arr[i][0]:2}, {arr[i][1]:2}]: top {arr[t]} 이 가장 외부입니다 k={k}")
    #     continue

    # ST 내 오른쪽 내부에 속하는 원 pop
    while len(ST) > 0:
        t = ST[-1]
        ts, te = arr[t][0]-arr[t][1], arr[t][0]+arr[t][1]
        if ts >= s and arr[t][0] <= arr[t][0]:
            sm = ST.pop()
            tmp -= arr[i][1]
            p = sm
            print(f"[{arr[i][0]:2}, {arr[i][1]:2}]: 오른쪽 내부 원 pop {arr[sm]}, k={tmp}")
        else:
            break

    # top 원의 왼쪽 내부에 속하지 않으면 1세트 끝
    if arr[t][0]+arr[t][1] <= s:
        # k == top[r] 체크
        print(f"[{arr[i][0]:2}, {arr[i][1]:2}]: 1세트 종료")
        tmp = 0
        # continue

    # 마지막 원이어도 1세트 끝
    if i == N-1:
        print(f"[{arr[i][0]:2}, {arr[i][1]:2}]: 1세트 종료")

    ST.append(i)
    tmp += arr[i][1]
    print(f"[{arr[i][0]:2}, {arr[i][1]:2}]: ({s:4}, {e:4}) | {ST} | {tmp}")
    prev = i


print(ST)
print(ans+1, tmp)
