import sys


def wrap_up():
    cnt = 0
    while stack:
        print(stack)
        next = stack.pop()
        if stack and next[0]+next[1] <= stack[-1][0]+stack[-1][1]:
            stack[-1][2] += next[1]  # 내부에 속하는 원
            print("right child")
        if stack and stack[-1][1] == stack[-1][2]:
            print("k+1")
            cnt += 1
    return cnt


N = int(input())
X = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
X.sort()

stack = []
answer = 0
for i in range(N):
    x, r = X[i][0], X[i][1]  # 현재 원의 좌표
    answer += 1
    print(stack, "curr:", X[i])

    if not stack:
        stack.append([x, r, 0])
        continue

    top = stack[-1]
    if top[0]-top[1] >= x-r:  # left include
        k = 0
        while top and top[0]-top[1] >= x-r:
            inner = stack.pop()
            k += inner[1]  # 반지름의 길이
            top = stack[-1] if stack else None
        stack.append([x, r, k])

    # elif top[0]+top[1] >= x+r:  # right include
    #     stack[-1][2] += r
    #     print("**", stack[-1])
    #     if stack[-1][1] == stack[-1][2]:
    #         answer += 1
    #         print("k+1")
    #     continue

    elif top[0]-top[1] < x-r:  # exclude
        print("need to wrap up!")
        stack.append([x, r, 0])
        # if wrap_up() > 0:
        answer += wrap_up()

    else:
        stack.append([x, r, 0])


# final wrap up
if stack:
    answer += wrap_up()

print(answer+1)  # 마지막 바깥 영역까지 !
