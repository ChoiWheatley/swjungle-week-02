from collections import deque
import sys


def mapper(string: str):
    x, c = string.split()
    # D배열 자료형 str -> int
    # L이면 0 R이면 1
    return [int(x), 0 if c == "L" else 1]


def tonum(string: str):
    global N
    r, c = string.split()
    return (int(r)-1) * N + int(c)


# 입력값
N = int(input())
K = int(input())
A = [tonum(sys.stdin.readline()) for _ in range(K)]
L = int(input())
D = deque([mapper(sys.stdin.readline()) for _ in range(L)])


# 상하좌우 이동
direc = ["U", "D", "R", "L"]  # 0 1 2 3
change = [[3, 2, 0, 1], [2, 3, 1, 0]]
move = [(0, -1), (0, 1), (1, 0), (-1, 0)]

# 위치 초기화
trace = deque([])
x, y = 1, 1
head = 2  # R
sec = 0  # 초 재기
while 0 < x < N+1 and 0 < y < N+1:
    # 방향 전환
    if D and sec == D[0][0]:
        d = D[0][1]  # L or D
        head = change[d][head]
        D.popleft()

    # 직진
    trace.append(N*(y-1)+x)
    x += move[head][0]
    y += move[head][1]
    sec += 1

    num = N*(y-1)+x
    # exceptions
    if num in trace:  # 꼬리와 닿으면 게임 종료
        break
    if num in A:  # 사과를 먹었다면
        A.remove(num)
    else:
        trace.popleft()


print(sec)
