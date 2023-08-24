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
    histogram = TC[1:]+[0]  # 현재 인덱스의 이전 인덱스까지 처리 -> 마지막에 0을 하나 더 붙여 준다.
    stack = []
    max_area = 0

    for i in range(N+1):
        curr = histogram[i]

        if not stack:
            stack.append(i)
            continue

        t = stack[-1]
        # curr가 top보다 작다
        if histogram[t] > curr:
            top = histogram[t]
            # top이 curr보다 작을때까지
            # 즉, curr보다 크거나 같은 것을 빼면서 최대 넓이를 구한다
            while stack:
                p = stack.pop()
                top = histogram[p]

                start = stack[-1] if stack else -1  # stack의 0번 인덱스까지 검사해야 합니다.
                max_area = max(max_area, top*(i-start-1))

                if top < curr:
                    stack.append(p)
                    break

        stack.append(i)

    print(max_area)
