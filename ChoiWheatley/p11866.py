"""요세푸스 수열을 구하는 프로그램. deque.rotate 사용하면 될 듯
어차피 K <= 1000밖에 되지 않아서 걍 전부 순회 돌면 될 것 같다."""
from typing import List
from collections import deque


def sol(k: int, n: int) -> List[int]:
    queue = deque((i for i in range(1, n + 1)))
    result = []
    while queue:
        queue.rotate(-k + 1)
        result.append(queue[0])
        queue.popleft()

    return result


if __name__ == "__main__":
    n, k = [int(x) for x in input().split()]
    print(f"<{', '.join([str(i) for i in sol(k, n)])}>")
