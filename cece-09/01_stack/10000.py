import sys

N = int(input())
X = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    x, r = X[i]
    X[i] = (x+r, 2*r)  # 끝점과 지름을 저장

X.sort()  # 끝점순으로, 지름 작은 순으로 오름차순 정렬


stack = []
answer = 0
for circle in X:
    tmp = circle[0]  # 첫 번째 원의 끝점
    is_complete = False

    while stack:
        top = stack.pop()

        if circle[0]-circle[1] <= top[0]-top[1]:  # 만약 circle 시작점이 더 작으면
            if tmp == top[0]:
                # top은 circle에 포함된다 -> 다시 검사할 필요 없다
                # 만약 끝점이 같으면 내접한다
                tmp = top[0]-top[1]  # top의 시작점으로 갱신

        else:
            stack.append(top)
            break  # 외부에 있는 원은 stack에 넣고 break한다

        if tmp == circle[0]-circle[1]:
            is_complete = True

    answer += 1
    if is_complete:
        answer += 1
    stack.append(circle)

print(answer+1)
