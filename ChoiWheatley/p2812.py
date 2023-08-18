def sol(n: str, k: int) -> int:
    """n에서 k개의 숫자를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다"""
    stack = []
    for digit in (int(x) for x in n):
        while k > 0 and len(stack) > 0 and digit > stack[-1]:
            k -= 1
            stack.pop()
        stack.append(digit)
    while k > 0:
        k -= 1
        stack.pop()
    return int("".join([str(x) for x in stack]))


if __name__ == "__main__":
    _, k = input().split()
    n = input()

    k = int(k)

    print(sol(n, k))
