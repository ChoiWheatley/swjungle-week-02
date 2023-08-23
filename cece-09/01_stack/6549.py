import sys

'''
1. 막대를 순서대로 스택에 push
2. push하려는 막대의 높이가 스택의 top인덱스의 막대 높이보다 크거나 같으면 쌓는다
3. push하려는 막대의 높이가 스택의 top보다 작을 경우, while을 돌면서 max를 갱신
'''
while True:
    TC = list(map(int, sys.stdin.readline().split()))

    if TC[0] == 0:
        exit()

    N = TC[0]
    histogram = TC[1:]+[0]

    stack = []

    max_area = 0
    min_height = float('inf')  # 현재 stack에 있는 것 중 최소높이

    for i in range(N+1):
        curr = histogram[i]

        if not stack:
            stack.append(i)
            print(f"[{i}] {curr}는 새로운 막대 | {stack}")
            continue

        t = stack[-1]
        # curr가 top보다 작다
        if histogram[t] > curr:
            print(f"[{i}] {curr}는 top보다 작다 | {stack}")
            top = histogram[t]
            # top이 curr보다 작을때까지
            # 즉, curr보다 크거나 같은 것을 빼면서 최대 넓이를 구한다
            while stack and top >= curr:
                chk = stack[-1]
                p = stack.pop()
                top = histogram[p]
                if stack:
                    max_area = max(
                        max_area, histogram[chk]*((i+1)-(stack[-1]+1)-1))
                print(f"  stack에서 pop [{p}] {top}, max={max_area} | {stack}")

        # curr가 top보다 크거나 같다, stack에 push
        else:
            print(f"[{i}] {curr}는 top보다 크거나 같다 | {stack}")
        stack.append(i)

    print(max_area)
