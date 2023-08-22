from collections import deque
import sys
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)] #노드 연결정보 저장
dist = [float('inf')] * (n + 1)  # 시작노드에서 각 노드까지 최단거리 저장리스트

for  _ in range(m):
    a,b,w = map(int,sys.stdin.readline().split())
    graph[a].append((b,w)) #그래프에 연결정보 추가

s,e = map(int,input().split())

def dijkstra(start):
    dist[start]=0
    q=[(0,s)] #디스트 초기화,q에 시작노드와 거리0

    while q: #우선순위 q가 빌떄까지 반복
        w, cur = heapq.heappop(q) #현재 노드와 거리정보를 큐에서 꺼냄
        
        if dist[cur]<w: #현재노드의 거리정보가 기존에 저장된 거리보다 크다면 스킵
            continue

        for dest,wei in graph[cur]:
            cost = dist[cur]+wei #새로운 거리 계산
            if dist[dest]>cost: # 새로운거리가 기존에 저장된 거리보다 작다면, 해당 노드의 거리를 업데이트
                dist[dest] = cost
                heapq.heappush(q,(cost,dest))#우선순위 큐에 추가

dijkstra(s)
print(dist[e])