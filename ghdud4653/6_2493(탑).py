#순회를 돌면서 인덱스와 탑의 높이를 튜플로 저장
#스택에 있는 탑들의 높이를 현재 탑의 높이와 비교
#현재 탑보다 작은 이전 탑들에서는 신호를 수신 받을 수 없으르몰 스택에서 제거
#현재 탑보다 크거나 같은 탑은 현재탑에서 신호를 수신 받을 수 있으므로 수신받는 탑의 인덱스를 +1을 정답에 저장

import sys
input = sys.stdin.readline

n = int(input())
top  = list(map(int,input().split()))

answer = [0]*n
stack=[]

for i in range(len(top)):
    while stack:
        if top[stack[-1][0]]<top[i]:# 마지막에 저장된 튜플
            stack.pop()
        else:
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,top[i]))
print(*answer)