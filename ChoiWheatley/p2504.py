"""재귀재귀"""


class InvalidParan(Exception):
    pass


def r_sol(s: str) -> int:
    if s == "":
        return 1

    # 유효한지 여부는 예외를 발생시키는 것으로 처리할 예정.
    # 구간 [i,j)에서 묶이는 올비른 괄호열의 그룹이 어디까지인지를 포착.
    i = 0
    stack = []
    multiply = 1
    result = 0
    for j, chr in enumerate(s):
        match chr:
            case "(":
                stack.append(2)
            case "[":
                stack.append(3)
            case ")":
                multiply = stack[-1]
                if multiply != 2:
                    raise InvalidParan()
                stack.pop()
            case "]":
                multiply = stack[-1]
                if multiply != 3:
                    raise InvalidParan()
                stack.pop()
        if len(stack) == 0:
            result += multiply * r_sol(s[i + 1 : j])
            i = j + 1
    return result


try:
    print(r_sol(input()))
except (IndexError, InvalidParan):
    print(0)
