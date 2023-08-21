#이해못함

from collections import deque

k = int(input())  # 테스트 케이스의 개수를 입력받습니다.

def bfs(graph, start):
    queue = deque()
    queue.append(start)
    if visited[start] == 0:
        visited[start] = 1  # 방문하지 않은 정점은 1번 그룹으로 표시
    while queue:
        v = queue.popleft()  # 큐에서 정점을 꺼냄

        color = visited[v]  # 현재 정점의 그룹
        for i in graph[v]:  # 현재 정점과 연결된 모든 정점을 확인
            if visited[i] == 0:  # 아직 방문하지 않은 정점일 경우
                queue.append(i)  # 다음에 방문할 정점으로 큐에 추가
                if color == 1:  # 현재 정점과 다른 그룹으로 색칠
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1:  # 이미 방문한 정점이 1번 그룹에 속한 경우
                if color == 1:  # 현재 정점도 1번 그룹이라면 이분 그래프가 x
                    print("NO")
                    return False
            elif visited[i] == 2:  # 이미 방문한 정점이 2번 그룹에 속한 경우
                if color == 2:  # 현재 정점도 2번 그룹이라면 이분 그래프가 x
                    print("NO")
                    return False
    return True

for i in range(k):
    flag = 0
    V, E = map(int, input().split())  # 정점의 개수 V와 간선의 개수 E를 입력
    graph = [[] for _ in range(V + 1)]  # 노드 연결 정보를 저장하는 리스트 초기화
    visited = [0] * (V + 1)  # 각 노드의 방문 여부와 그룹을 나타내는 리스트 초기화
    for j in range(E):
        a, b = map(int, input().split())  # 간선 정보 입력받음
        graph[a].append(b)  # 노드 a와 b를 연결하는 양방향 간선 추가
        graph[b].append(a)  # 양방향 그래프이므로 b와 a도 연결해줌
    for k in range(1, V + 1):  # 연결그래프일 경우에는 시작점에서 한 번의 BFS를 수행
        if not bfs(graph, k):  # 비연결그래프의 경우에는 모든 정점을 탐색
            flag = 1
            break
    if flag == 0:
        print("YES")
