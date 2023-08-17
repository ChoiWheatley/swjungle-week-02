import sys
N = int(input())
X = [int(sys.stdin.readline()) for _ in range(N)]
ST = []

for i in range(N):
    # stack is empty
    if len(ST) == 0:
        ST.append(X[i])
        continue
    # while top <= curr, pop all smallers
    top = ST[-1]
    while top <= X[i]:
        ST.pop()
        if len(ST) == 0:
            break
        top = ST[-1]
    # push
    ST.append(X[i])

print(len(ST))
