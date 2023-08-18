def is_vps(s: str) -> bool:
    stack = []
    try:
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                stack.pop()
        return len(stack) == 0
    except IndexError:
        return False


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print("YES" if is_vps(input()) else "NO")
