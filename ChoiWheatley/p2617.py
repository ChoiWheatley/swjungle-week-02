"""
구슬 찾기

플로이드 워셜 알고리즘이라는 말을 들었다. 한 번 구현해본 적 있으니 괜찮으려나?
"""
from sys import maxsize, stdin
from bitset2d import Bitset2D

INF = maxsize


def sol(graph: Bitset2D, N: int, M: int) -> int:
    """
    G[i][j] 가 연결되어있는지를 저장한 희소행렬을 사용하여 i -> j로 가는 비용을 계산한다.

    이때 비용 w가 전체 간선의 개수 M의 과반을 넘는다면 i, j는 빼도 되는 구슬들이다.

    - N: 구슬의 개수
    - M: 간선의 개수
    """

    in_dist = [[INF for _ in range(N)] for _ in range(N)]
    out_dist = [[INF for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            in_dist[i][j] = 1 if graph.get2d(i, j) else INF
            out_dist[j][i] = 1 if graph.get2d(i, j) else INF

    for k in range(N):
        for i in range(N):
            for j in range(N):
                in_dist[i][j] = min(in_dist[i][j], in_dist[i][k] + in_dist[k][j])
                out_dist[i][j] = min(out_dist[i][j], out_dist[i][k] + out_dist[k][j])

    result = set()
    for i in range(N):
        if len([x for x in in_dist[i] if x != INF]) > N // 2:
            result.add(i)
        if len([x for x in out_dist[i] if x != INF]) > N // 2:
            result.add(i)

    return len(result)


if __name__ == "__main__":
    n, m = (int(x) for x in stdin.readline().split())
    graph = Bitset2D(n, n)

    for _ in range(m):
        i, j = (int(x) for x in stdin.readline().split())
        graph.set2d(i - 1, j - 1)

    print(sol(graph, n, m))
