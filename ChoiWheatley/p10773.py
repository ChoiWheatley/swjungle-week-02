from sys import stdin

g_stack = []

k = int(input())
for _ in range(k):
    op = int(stdin.readline().strip())
    if op == 0:
        g_stack.pop()
        continue
    g_stack.append(op)

print(sum(g_stack))
