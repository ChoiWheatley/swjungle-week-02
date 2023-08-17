S = input()
STX = []
# STY = []


def empty():
    return len(STX) == 0


answer = 0
last = -1
for i in range(len(S)):
    if S[i] == "(":
        STX.append(S[i])
    if S[i] == "[":
        STX.append(S[i])
    if S[i] == ")":
        if empty():
            print(0)
            break
        top = STX.pop()
        if top == "(":
            if last == 0:
                answer = answer * 2
            if last == 1:
                answer = answer + 2
            if last == -1:
                answer = 2
            last = 0
        else:
            print(0)
            break
    if S[i] == "]":
        if empty():
            print(0)
            break
        top = STX.pop()
        if top == "[":
            if last == 0:
                answer = answer * 3
            if last == 1:
                answer = answer + 3
            if last == -1:
                answer = 3
            last = 0
        else:
            print(0)
            break
