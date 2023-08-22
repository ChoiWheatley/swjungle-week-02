"""줄 세우기"""


from sys import stdin


def r_sol(idx: int):
    global visited, stack, graph
    if idx in visited:
        return
    visited.add(idx)

    children = graph[idx]
    for child in children:
        if child in visited:
            continue
        r_sol(child)

    # 재귀를 다 돌리고 난 다음에 스택에 추가해야 순서가 맞다
    stack.append(idx)


n, m = (int(x) for x in stdin.readline().split())
graph = [[] for _ in range(n + 1)]  # index starts from 1
visited = set()
stack = []

for _ in range(m):
    pre, post = (int(x) for x in stdin.readline().split())
    graph[pre].append(post)


for i in range(1, n + 1):
    r_sol(i)

print(" ".join(str(x) for x in reversed(stack)))
