"""항상 top보다 작아야함"""

g_stack = []

n = int(input())
for _ in range(n):
    new = int(input())
    while len(g_stack) > 0 and new >= g_stack[-1]:
        g_stack.pop()


print(len(g_stack))
