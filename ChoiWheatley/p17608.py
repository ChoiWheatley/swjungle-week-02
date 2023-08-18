"""항상 top보다 작아야함"""
from sys import stdin

g_stack = []

n = int(stdin.readline().strip())
ls = [int(stdin.readline().strip()) for _ in range(n)]
for new in ls:
    while len(g_stack) > 0 and new >= g_stack[-1]:
        g_stack.pop()
    g_stack.append(new)


print(len(g_stack))
