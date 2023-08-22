#모르겠어요

import sys
input = lambda: sys.stdin.readline().rstrip()

# 입력에서 정점의 개수 V와 간선의 개수 E를 받음
V, E = map(int, input().split())

# 간선들의 정보를 담을 리스트를 초기화
edges = []

# E개의 간선 정보를 입력받아 리스트에 추가
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
    
# 간선을 비용(C)이 작은 순서대로 정렬
edges.sort(key=lambda x: x[2])

# 각 정점의 부모를 저장할 리스트를 초기화
parent = [i for i in range(V+1)]

# 특정 정점의 부모를 찾는 함수를 정의
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])  # 경로 압축을 통해 부모를 갱신
    return parent[x]

# 두 정점을 합치는 함수를 정의합니다.
def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:  # 작은 쪽이 부모가 되도록 설정 (같은 집합 관계라서 별도의 부모가 있는 것이 아님)
        parent[b] = a
    else:
        parent[a] = b        

# 두 정점이 같은 부모를 가지는지 확인하는 함수를 정의
def same_parent(a, b):
    return get_parent(a) == get_parent(b)

# MST의 총 비용을 저장할 변수를 초기화
answer = 0
# 정렬된 간선들을 하나씩 처리
for a, b, cost in edges:
    # cost가 작은 간선부터 하나씩 추가하면서 같은 부모를 공유하지 않을 때 (사이클이 없을 때)만 확정
    if not same_parent(a, b):
        union_parent(a, b)  # 두 정점을 연결합니다.
        answer += cost       # 간선 비용을 누적합니다.

# MST의 총 비용을 출력합니다.
print(answer)

answer = 0
for a, b, cost in edges:
    # cost가 작은 edge부터 하나씩 추가해가면서 같은 부모를 공유하지 않을 때(사이클 없을 때)만 확정
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)
