S = input()
ST = []

answer = 0
tmp = 1
prev = ""  # 직전 괄호를 검사
is_VPS = True
for i in range(len(S)):
    if S[i] == "(":
        tmp *= 2
        ST.append(S[i])
    if S[i] == "[":
        tmp *= 3
        ST.append(S[i])
    if S[i] == ")":
        if len(ST) == 0:
            is_VPS = False
            break
        top = ST[-1]
        if top == "(":  # 괄호 매칭되면 pop
            ST.pop()
            if prev == "(":  # () 매칭이면 answer로 더하기
                answer += tmp
        tmp //= 2  # 연산 완료되었으므로 // 2
    if S[i] == "]":
        if len(ST) == 0:
            is_VPS = False
            break
        top = ST[-1]
        if top == "[":
            ST.pop()
            if prev == "[":
                answer += tmp
        tmp //= 3
    prev = S[i]


if len(ST) > 0:  # 스택에 괄호가 남아있으면 not VPS
    is_VPS = False

if is_VPS:
    print(answer)
else:
    print(0)
