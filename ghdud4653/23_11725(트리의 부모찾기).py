
import sys
sys.setrecursionlimit(10**9)  # 최대 재귀 깊이를 설정

def dfs(v):
    visited[v] = 1  # 현재 노드를 방문했음을 표시
    for num in graph[v]:
        if not visited[num]:
            answer[num] = v  # 현재 노드를 다음 노드의 부모로 설정합
            dfs(num)

N = int(input())

graph = [[] for _ in range(N+1)]  # 노드의 연결 관계를 저장하는 리스트를 초기화
visited = [0 for _ in range(N+1)]  # 방문 여부를 나타내는 리스트를 초기화
answer = [1 for _ in range(N+1)]  # 각 노드의 부모 노드를 저장하는 리스트를 초기화

# 간선 정보를 입력받아 그래프를 구성합니다.
for i in range(N-1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 부모 노드의 값이 작은 순서로 정렬합니다.
for i in graph:
    i.sort()

dfs(1)  # DFS를 시작합니다. (시작 노드는 1번 노드로 설정)

# 루트 노드를 제외한 각 노드의 부모 노드를 출력합니다.
for i in range(2, len(answer)):
    print(answer[i])


dfs(1)

for i in range(2,len(answer)):
    print(answer[i])