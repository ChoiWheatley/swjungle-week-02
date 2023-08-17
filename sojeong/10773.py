import sys


K = int(input())
X = [int(sys.stdin.readline()) for _ in range(K)]
ST = []

for i in range(K):
    if X[i] == 0:
        ST.pop()
    else:
        ST.append(X[i])

print(sum(ST))
