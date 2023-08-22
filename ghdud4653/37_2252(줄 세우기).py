import sys
from collections import deque

N,M =map (int, sys.stdin.readline().split())

# 인접리스트와 진입 차수 배열 초기화
g = [[] for _ in range(N+1)]
d = [0 for _ in range(N+1)]

#노드의 진입 차수가 0 인경우 큐에 넣어 위상 절려 시작

q= deque()
ans = [] # 위상 정ㄹㄹ렬 결과를 저장할 리스트

#간선 정보 입력 진입 차수 계산
for i in range(M):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    g[a].append(b) # a에서 b로 가는 간선 정보 추가
    d[b]+=1  # b의 진입 차수 증가

#진입 차수가 0 인 노드들을 큐에 추가하여 위상 정렬 시장
for i in range(1,N+1):
    if d[i]==0:
        q.append(i)

while q:
    temp = q.popleft() #q에서 노드 추출
    ans.append(temp) #현재 노드 결과에 추가
    for i in g[temp]:
        d[i]-=1 # 현재 노드에서 나가는 간선 제거
        if d[i]==0:
            q.append(i) # 진입 차수가 0이 되면 큐에 추가하여 다음 단계로


#위상정렬 결과출력
print(*ans)



