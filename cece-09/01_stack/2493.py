N = int(input())
tower = list(map(int, input().split()))

ST = []
result = [0 for _ in range(N)]


for i in range(N):
    if i == 0:
        result[i] = 0
        ST.append(i+1)
        continue
    if not len(ST):
        result[i] = 0
        ST.append(i+1)
        continue
    # tower[i] 크기 비교
    top = tower[ST[-1]-1]
    if tower[i] > top:
        while top < tower[i]:
            ST.pop()
            if len(ST) == 0:
                break
            top = tower[ST[-1]-1]
        if len(ST) > 0:
            result[i] = ST[-1]
        else:
            result[i] = 0
        ST.append(i+1)
    else:
        result[i] = ST[-1]
        ST.append(i+1)

for i in range(N):
    print(result[i], end=' ')
