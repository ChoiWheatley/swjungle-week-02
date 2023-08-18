N = int(input())
PS = [input() for _ in range(N)]

for i in range(N):
    ST = []
    # l, s = 0
    is_VPS = True
    for p in PS[i]:
        if p == "(":
            ST.append(p)
            # l += 1
        elif p == ")":
            if len(ST) == 0:
                is_VPS = False
                break
            top = ST.pop()
            if top != "(":
                is_VPS = False
                break
    if len(ST) != 0:
        is_VPS = False
    if is_VPS:
        print("YES")
    else:
        print("NO")
