#모르겠어요

import sys
sys.setrecursionlimit(10 ** 9)  # 재귀 깊이 제한을 늘림
input = sys.stdin.readline

tree = []
while True:
    try:
        tree.append(int(input()))
    except:
        break

def post(start, end):
    if start > end:
        return
    mid = end + 1
    for i in range(start + 1, end + 1):
        if tree[i] > tree[start]:
            mid = i
            break
    post(start + 1, mid - 1)  # 왼쪽 서브트리 탐색
    post(mid, end)  # 오른쪽 서브트리 탐색
    print(tree[start])  # 루트 노드 출력

post(0, len(tree) - 1)  # 전위 순회 결과를 토대로 후위 순회 수행
