'''
parent가 child보다 무거운 트리 만들기
ex) 2-1과 5-1 간선이 순서대로 주어졌다면
    2-5-1 parent[1] = 5, parent[5] = 2 순으로 정렬되어야 한다.
'''

N, M = map(int, input().split())

parent = [i for i in range(N)]
child = [i for i in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    parent[v-1] = u-1
    child[u-1] = v-1

print(parent)
print(child)

for i in range(N):
    if i == parent[i]:
        print("no parent", i+1)
    if i == child[i]:
        print("no child", i+1)
