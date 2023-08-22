# import sys

# ''''
# pseudo
# case 1 if empty:  push
# case 2 while 오른쪽 내부 원이 stack에 있음: pop all while sum up r and push this with result
# case 3 if 외접 or 떨어져 있으면: pop all from stack

# '''
# N = int(input())
# C = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# # x좌표를 기준으로 정렬
# C.sort(key=lambda a: a[0])


# ST = []

# # 주어진 모든 원에 대해 차례대로 검사

# tmp = 0  # 내부 반지름을 합산하는 데 사용
# ans = 0  # 영역 합산
# p = -1  # 직전 원 인덱스

# # first push
# # ST.append((0, 0))

# for i in range(N+1):
#     if i == N:
#         tmp = ST[-1][0]
#         while ST:
#             # print(C[ST[-1][1]][0]+C[ST[-1][1]][1])
#             lk, l = ST.pop()  # leftmost
#             print(f"{C[l]} lk={lk}")
#             if not ST:
#                 break
#             if C[l][0]+C[l][1] <= C[ST[-1][1]][0]+C[ST[-1][1]][1]:
#                 tmp += C[l][1]  # 반지름을 더함
#         print(tmp)

#     ans += 1
#     x, r = C[i][0], C[i][1]
#     s, e = x-r, x+r
#     print(f"[{i}] ({x}, {r})")

#     if not ST:
#         ST.append((i, 0))
#         continue

#     # tk, t = ST[-1]  # top 원
#     # tx, tr = C[t][0], C[t][1]
#     # ts, te = tx-tr, tx+tr  # 원이 차지하는 구간

#     total_k = 0
#     while ST and C[ST[-1][1]][0]-C[ST[-1][1]][1] >= s:
#         pk, p = ST.pop()  # ST 내 오른쪽 내부에 속하는 원 pop
#         total_k += C[p][1]
#         # p = sm
#         print(f"  오른쪽원 {C[p]} pop (k={total_k})")

#     # top 원의 왼쪽 내부에 속하지 않으면 1세트 끝
#     while ST and C[ST[-1][1]][0]+C[ST[-1][1]][1] <= s:
#         # print(C[ST[-1][1]][0]+C[ST[-1][1]][1])
#         lk, l = ST.pop()  # leftmost
#         print(f"{C[l]} lk={lk}")
#         if C[l][0]+C[l][1] <= C[ST[-1][1]][0]+C[ST[-1][1]][1]:
#             ST[-1][0] += C[l][1]  # 반지름을 더함
#         if len(ST) == 1:
#             print(f"  {ST[-1]}")
#             break

#     ST.append((total_k, i))
#     print(f"  ST:{ST}")


# print(ST)
# print(ans+1, tmp)
