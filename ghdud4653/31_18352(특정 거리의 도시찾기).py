from collections import deque
import sys
n,m,dist,start = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
distance = [0]*(n+1)
for  _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)


def bfs(n,k):
    answer = []
    queue = deque()
    queue.append(n)
    distance[n] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if distance[i] == 0:
                queue.append(i)
                distance[i] = distance[now]+1
                if distance[i] == k:
                    answer.append(i)

                    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i,end='\n')

bfs(start,dist)
            